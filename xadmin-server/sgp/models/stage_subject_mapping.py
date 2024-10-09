from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Stage_Subject_Mapping(DbSgpBaseModel):
    stage_id = models.BigIntegerField(verbose_name=_("学段"), null=True, blank=True)
    subject_id = models.BigIntegerField(verbose_name=_("科目"), null=True, blank=True)

    class Meta:
        verbose_name = _("stage_subject_mapping")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.stage_id}-{self.subject_id}"