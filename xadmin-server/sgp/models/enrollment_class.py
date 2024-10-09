from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Enrollment_Class(DbSgpBaseModel):
    enrollment_year = models.BigIntegerField(verbose_name=_("入学年级"), null=True, blank=True)
    enrollment_class_number = models.BigIntegerField(verbose_name=_("班级"), null=True, blank=True)
    school_id = models.BigIntegerField(verbose_name=_("学校"), null=True, blank=True)
    enrollment_class_name = models.CharField(verbose_name=_("班级别名"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("enrollment_class")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.school_id}-{self.enrollment_year}-{self.enrollment_class_number}"