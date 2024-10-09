from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Student_Enrollment_Class_Mapping(DbSgpBaseModel):
    student_id = models.BigIntegerField(verbose_name=_("学生"), null=True, blank=True)
    enrollment_class_id = models.BigIntegerField(verbose_name=_("班级"), null=True, blank=True)
    grade_semester_id = models.BigIntegerField(verbose_name=_("年级描述"), null=True, blank=True)
    start_time = models.DateField(verbose_name=_("开始时间"), null=True, blank=True)
    end_time = models.DateField(verbose_name=_("结束时间"), null=True, blank=True)

    class Meta:
        verbose_name = _("student_enrollment_class_mapping")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.student_id}-{self.enrollment_class_id}-{self.grade_semester_id}"