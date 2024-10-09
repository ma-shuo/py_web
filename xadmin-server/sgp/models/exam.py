from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Exam(DbSgpBaseModel):
    exam_type_id = models.BigIntegerField(verbose_name=_("考试类型"), null=True, blank=True)
    exam_time = models.DateField(verbose_name=_("考试时间"), null=True, blank=True)
    exam_name = models.CharField(verbose_name=_("考试名称"), max_length=255, null=True, blank=True)
    enrollment_year = models.BigIntegerField(verbose_name=_("入学年级"), null=True, blank=True)
    grade_semester_id = models.BigIntegerField(verbose_name=_("年级描述"), null=True, blank=True)

    class Meta:
        verbose_name = _("Exam")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.exam_name}"