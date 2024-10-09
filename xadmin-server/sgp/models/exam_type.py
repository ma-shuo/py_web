from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Exam_Type(DbSgpBaseModel):
    exam_type_name = models.CharField(verbose_name=_("考试类型"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("exam_type")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.exam_type_name}"