from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Exam_Stage_Subject_Mapping(DbSgpBaseModel):
    stage_subject_mapping_id = models.BigIntegerField(verbose_name=_("学段_科目关系id"), null=True, blank=True)
    exam_id = models.BigIntegerField(verbose_name=_("考试名称"), null=True, blank=True)

    class Meta:
        verbose_name = _("exam_stage_subject_mapping")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.stage_subject_mapping_id}-{self.exam_id}"