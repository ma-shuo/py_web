from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Grade_Semester(DbSgpBaseModel):
    grade_name = models.CharField(verbose_name=_("名称"), max_length=255, null=True, blank=True)
    semester_name = models.CharField(verbose_name=_("学期"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("grade_semester")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.grade_name}-{self.semester_name}"