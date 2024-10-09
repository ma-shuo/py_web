from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Teacher(DbSgpBaseModel):
    teacher_name = models.CharField(verbose_name=_("教师姓名"), max_length=255, null=True, blank=True)
    school_id = models.BigIntegerField(verbose_name=_("学校"), null=True, blank=True)

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.teacher_name}"