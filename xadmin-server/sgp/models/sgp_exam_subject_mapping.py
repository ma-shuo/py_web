from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Sgp_Exam_Subject_Mapping(DbSgpBaseModel):
    in_exam_stage_subject_mapping_id = models.BigIntegerField(verbose_name=_("入口考试科目"), null=True, blank=True)
    out_exam_stage_subject_mapping_id = models.BigIntegerField(verbose_name=_("出口考试科目"), null=True, blank=True)

    class Meta:
        verbose_name = _("sgp_exam_subject_mapping")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.in_exam_stage_subject_mapping_id}-{self.out_exam_stage_subject_mapping_id}"