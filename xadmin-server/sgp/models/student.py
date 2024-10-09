from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Student(DbSgpBaseModel):
    title = models.CharField(verbose_name=_("Menu title"), max_length=255, null=True, blank=True)
    icon = models.CharField(verbose_name=_("Left icon"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.title}-{self.description}"