import math
import hashlib
import pandas as pd
from django.db import connection
from datetime import datetime

from common.utils.timezone import convert_date
from sgp.models import *





# 学段-年级-年级描述-考试类型-考试时间-姓名/学号
# name = '初中-2022-七年级下学期-期末考试-20230624-学号.xls'
name = '初中-2022-八年级-上学期-期末考试-20240122-学号.xls'
keywords = name.split('.')[0].split('-')

type_method = keywords[6]
def read_excel():
    df = pd.read_excel('~/com/0929/'+name)

    if type_method == '姓名':
        duplicates = df.duplicated(subset=['学校', '姓名'], keep=False)
        # 只保留未标记为重复的行
        df = df[~duplicates]

    dic = {
        'school': [],
        'cl': {},
        'student': [],
        'type': []
    }

    header = df.columns.tolist()
    dic['type'] = header[4:]
    df['学号'] = df['学号'].astype(str)
    for index, row in df.iterrows():
        dic['school'].append(row['学校'])

        if type_method == '姓名':
            md5_hash = hashlib.md5()
            str_info = row['姓名'] + row['学校'] + keywords[0].split('级')[0]
            md5_hash.update(str_info.encode('utf-8'))
            row['学号'] = md5_hash.hexdigest()


        dic['student'].append(row)
        dic['cl'][row['学校']] = []

    for index, row in df.iterrows():
        dic['school'].append(row['学校'])
        # dic['cl'][row['学校']].append(int(row['班级']))
        if not math.isnan(row['班级']):
            int_value = int(row['班级'])  # 安全地转换为整数
        else:
            # 处理NaN的情况，例如设置一个默认值或者抛出一个错误
            int_value = 1  # 或者其他适当的处理方式
        dic['cl'][row['学校']].append(int_value)

    # 学校去重
    dic['school'] = list(set(dic['school']))
    # 班级去重
    for key in dic['cl']:
        dic['cl'][key] = list(set(dic['cl'][key]))


    dic['level'] = keywords[0]
    dic['great'] = keywords[1]
    dic['great_name'] = keywords[2]
    dic['great_type'] = keywords[3]
    dic['mold'] = keywords[4]
    dic['time'] = keywords[5]
    dic['name'] = name.split('.')[0]

    return dic


def add_data_sql(dic):
    print('开始时间：', datetime.now())
    print("====================新增学校===============")
    # 新增学校
    school = dic['school']
    for entry in school:
        school, created = School.objects.get_or_create(school_name=entry)
        school, created = School_Stage_Mapping.objects.get_or_create(school_id=school.id, stage_id=Stage.objects.get(stage_name=dic['level']).id)

    # 新增班级
    print("====================新增班级===============")
    cl = dic['cl']
    data = []
    for key in cl:
        for entry in cl[key]:
            school = School.objects.get(school_name=key)
            k, created = Enrollment_Class.objects.get_or_create(
                enrollment_year=dic['great'],
                enrollment_class_number=entry,
                school_id=school.id,
                enrollment_class_name=''
            )

    # 学生表
    print("====================新增学生===============")
    student = dic['student']
    for entry in student:
        school, created = Student.objects.get_or_create(student_name=entry['姓名'], school_issued_student_id=entry['学号'])

    # 学生-班级关系表
    print("====================新增学生-班级关系===============")
    data = []
    for e in dic['student']:
        student = Student.objects.get(student_name=e['姓名'], school_issued_student_id=e['学号'])
        school = School.objects.get(school_name=e['学校'])
        cl = Enrollment_Class.objects.get(school_id=school.id, enrollment_class_number=e['班级'], enrollment_year=dic['great'])
        gr = Grade_Semester.objects.get(grade_name=dic['great_name'], semester_name=dic['great_type'])
        Student_Enrollment_Class_Mapping.objects.get_or_create(
            student_id=student.id,
            enrollment_class_id=cl.id,
            grade_semester_id=gr.id,
            start_time='2024-01-01',
            end_time='2024-01-28'
        )

    # 考试表
    print("====================新增考试===============")
    ks_data = []
    id = Exam_Type.objects.get(exam_type_name=dic['mold'])
    gr = Grade_Semester.objects.get(grade_name=dic['great_name'], semester_name=dic['great_type'])
    Exam.objects.get_or_create(
        exam_type_id=id.id,
        exam_time=convert_date(dic['time']),
        defaults={'exam_name': dic['name']},
        grade_semester_id=gr.id,
        enrollment_year=dic['great']
    )

    # 考试科目表
    print("====================新增考试科目===============")
    for e in dic['type']:
        t, created = Exam_Stage_Subject_Mapping.objects.get_or_create(
            stage_subject_mapping_id=Stage_Subject_Mapping.objects.get(
                subject_id=Subject.objects.get(subject_name=e).id,
                stage_id=Stage.objects.get(stage_name=dic['level']).id
            ).id,
            exam_id=Exam.objects.get(
                        exam_type_id=Exam_Type.objects.get(exam_type_name=dic['mold']).id,
                        exam_time=convert_date(dic['time']),
                        grade_semester_id=Grade_Semester.objects.get(grade_name=dic['great_name'], semester_name=dic['great_type']).id,
                        enrollment_year=dic['great']
                    ).id
        )

    # 成绩表
    print("====================新增成绩===============")
    data = []
    for k in dic['type']:
        test_name = Exam.objects.get(
            exam_type_id=Exam_Type.objects.get(exam_type_name=dic['mold']).id,
            exam_time=convert_date(dic['time']),
            grade_semester_id=Grade_Semester.objects.get(grade_name=dic['great_name'], semester_name=dic['great_type']).id,
            enrollment_year=dic['great']
        )
        exam_subject = Exam_Stage_Subject_Mapping.objects.get(
            stage_subject_mapping_id=Stage_Subject_Mapping.objects.get(
                subject_id=Subject.objects.get(subject_name=k).id,
                stage_id=Stage.objects.get(stage_name=dic['level']).id
            ).id,
            exam_id=test_name.id
        )
        for i, e in enumerate(dic['student']):
            s = Student_Enrollment_Class_Mapping.objects.filter(
                student_id=Student.objects.get(school_issued_student_id=e['学号'], student_name=e['姓名']).id,
                start_time__lte=convert_date(dic['time']),
                end_time__gte=convert_date(dic['time'])
            ).first()
            print(s)
            data.append(Exam_Subject_Score(
                student_enrollment_class_mapping_id=s.id,
                exam_stage_subject_mapping_id=exam_subject.id,
                raw_score=e[k], standard_score=0),)
            if(i % 100 == 0):
                print(i, '/', len(dic['student']))
    Exam_Subject_Score.objects.bulk_create(data)
    print('============success==============')
    print('完成时间：', datetime.now())
