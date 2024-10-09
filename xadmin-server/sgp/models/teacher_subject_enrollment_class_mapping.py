from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Teacher_Subject_Enrollment_Class_Mapping(DbSgpBaseModel):
    enrollment_class_id = models.BigIntegerField(verbose_name=_("班级"), null=True, blank=True)
    teacher_id = models.BigIntegerField(verbose_name=_("教师"), null=True, blank=True)
    stage_subject_mapping_id = models.BigIntegerField(verbose_name=_("学段科目"), null=True, blank=True)
    start_time = models.DateField(verbose_name=_("开始时间"), null=True, blank=True)
    end_time = models.DateField(verbose_name=_("结束时间"), null=True, blank=True)

    class Meta:
        verbose_name = _("teacher_subject_enrollment_class_mapping")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.enrollment_class_id}-{self.teacher_id}-{self.stage_subject_mapping_id}"