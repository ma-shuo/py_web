from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Stage(DbSgpBaseModel):
    stage_name = models.CharField(verbose_name=_("学段"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("Stage")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.stage_name}"