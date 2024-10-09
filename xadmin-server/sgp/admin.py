from django.contrib import admin

# Register your models here.
from sgp.models import *

admin.site.register(Enrollment_Class)
admin.site.register(Exam)
admin.site.register(Exam_Stage_Subject_Mapping)
admin.site.register(Exam_Subject_Score)
admin.site.register(Exam_Type)
admin.site.register(Grade_Semester)
admin.site.register(School)
admin.site.register(School_Stage_Mapping)
admin.site.register(Sgp_Exam_Subject_Mapping)
admin.site.register(Sgp_Score)
admin.site.register(Stage)
admin.site.register(Stage_Subject_Mapping)
admin.site.register(Student)
admin.site.register(Student_Enrollment_Class_Mapping)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Teacher_Subject_Enrollment_Class_Mapping)