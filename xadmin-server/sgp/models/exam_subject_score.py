from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel
from decimal import Decimal, ROUND_HALF_UP



class Exam_Subject_Score(DbSgpBaseModel):
    student_enrollment_class_mapping_id = models.BigIntegerField(verbose_name=_("学生_班级关系id"), null=True, blank=True)
    exam_stage_subject_mapping_id = models.BigIntegerField(verbose_name=_("考试_学段_科目关系id"), null=True, blank=True)
    raw_score = models.DecimalField(verbose_name=_("原始分"), max_digits=6, decimal_places=2, default=0)
    standard_score = models.DecimalField(verbose_name=_("标准分"), max_digits=6, decimal_places=2, default=0)

    class Meta:
        verbose_name = _("exam_subject_score")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.student_enrollment_class_mapping_id}-{self.exam_stage_subject_mapping_id}"