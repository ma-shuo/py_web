from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Sgp_Score(DbSgpBaseModel):
    student_enrollment_class_mapping_id = models.BigIntegerField(verbose_name=_("sgp人员"), null=True, blank=True)
    sgp_score = models.CharField(verbose_name=_("sgp成绩"), max_length=255, null=True, blank=True)
    sgp_exam_subject_mapping_id = models.BigIntegerField(verbose_name=_("sgp考试科目"), null=True, blank=True)

    class Meta:
        verbose_name = _("sgp_score")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.student_enrollment_class_mapping_id}-{self.sgp_exam_subject_mapping_id}"