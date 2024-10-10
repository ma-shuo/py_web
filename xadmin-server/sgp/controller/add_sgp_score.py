from datetime import datetime

from django.db import connection

from common.utils.timezone import convert_date
from sgp.models import *
import pandas as pd


name = 'SGP-2022-20240122_八年级_上学期_期末考试T20240705_八年级_下学期_期末考试-数学-初中-学号.xls'
# name = 'SGP-2022-20230222_七年级上学期_期末考试T20230624_七年级下学期_期末考试-地理-初中-学号.xls'
keywords = name.split('.')[0].split('-')
def read_sgp_excel():
    df = pd.read_excel(f'~/com/0929/{name}', engine='xlrd')
    dic = {
        'leval': keywords[1],
        'inlet': keywords[2].split('T')[0].split('_'),
        'outlet': keywords[2].split('T')[1].split('_'),
        'type': keywords[3],
        'status': keywords[4],
        'use_code': keywords[5],
        'data': []
    }
    for index, row in df.iterrows():
        dic['data'].append({
            'school': row['学校'],
            'cl': row['班级'],
            'name': row['姓名'],
            'sgp': row['SGP'],
            'code': row['学号']
        })
    return dic





def add_sgp_sql(dic):

    # 添加SGP考试科目记录
    学段科目 = Stage_Subject_Mapping.objects.get(
        subject_id=Subject.objects.get(subject_name=dic['type']).id,
        stage_id=Stage.objects.get(stage_name=dic['status']).id
    )

    入口考试科目 = Exam_Stage_Subject_Mapping.objects.get(
        stage_subject_mapping_id=学段科目.id,
        exam_id=Exam.objects.get(
            exam_type_id=Exam_Type.objects.get(exam_type_name=dic['inlet'][3]).id,
            exam_time=convert_date(dic['inlet'][0]),
            grade_semester_id = Grade_Semester.objects.get(grade_name=dic['inlet'][1], semester_name=dic['inlet'][2]).id,
            enrollment_year = dic['leval']
        ).id
    )

    出口考试科目 = Exam_Stage_Subject_Mapping.objects.get(
        stage_subject_mapping_id=学段科目.id,
        exam_id=Exam.objects.get(
            exam_type_id=Exam_Type.objects.get(exam_type_name=dic['outlet'][3]).id,
            exam_time=convert_date(dic['outlet'][0]),
            grade_semester_id = Grade_Semester.objects.get(grade_name=dic['outlet'][1], semester_name=dic['outlet'][2]).id,
            enrollment_year = dic['leval']
        ).id
    )

    info, created = Sgp_Exam_Subject_Mapping.objects.get_or_create(
        in_exam_stage_subject_mapping_id=入口考试科目.id,
        out_exam_stage_subject_mapping_id=出口考试科目.id
    )

    data = []
    print('开始时间：', datetime.now())
    for i, val in enumerate(dic['data']):
        if(i % 100 == 0):
            print('进度：', i, '/', len(dic['data']))

        # 班级 = 班级表.objects.get(学校=学校表.objects.get(学校=val['school']).id, 班级=val['cl'], 入学年级 = dic['leval'])
        st = Student_Enrollment_Class_Mapping.objects.filter(
            start_time__lte=convert_date(dic['outlet'][0]),
            end_time__gte=convert_date(dic['outlet'][0]),
            enrollment_class_id=Enrollment_Class.objects.get(
                school_id=School.objects.get(school_name=val['school']).id,
                enrollment_class_number=val['cl'],
                enrollment_year = dic['leval']).id
        )



        if dic['use_code'] == '姓名':
            st = st.filter(
                student_id=Student.objects.get(
                    student_name=val['name'],
                    school_issued_student_id=val['code']
                ).id
            )
        else:
            st = st.filter(
                student_id=Student.objects.get(
                    student_name=val['name'],
                    school_issued_student_id=val['code']
                ).id
            )
        data.append(
            Sgp_Score(
                sgp_score=val['sgp'],
                sgp_exam_subject_mapping_id=info.id,
                student_enrollment_class_mapping_id= st[0].id
            )
        )
    Sgp_Score.objects.bulk_create(data)
    print('开始时间：', datetime.now())
