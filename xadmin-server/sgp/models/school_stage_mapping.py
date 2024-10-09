from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class School_Stage_Mapping(DbSgpBaseModel):
    school_id = models.BigIntegerField(verbose_name=_("学校"), null=True, blank=True)
    stage_id = models.BigIntegerField(verbose_name=_("学段"), null=True, blank=True)

    class Meta:
        verbose_name = _("school_stage_mapping")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.school_id}-{self.stage_id}"