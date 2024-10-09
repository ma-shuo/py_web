from django.db import models
from django.utils.translation import gettext_lazy as _

from common.core.models import DbAuditModel, DbUuidModel


class SgpScore(models.Model):
    title = models.CharField(verbose_name=_("Menu title"), max_length=255, null=True, blank=True)
    description = models.CharField(verbose_name=_("Menu title"), max_length=255, null=True, blank=True)
    des = models.CharField(verbose_name=_("Menu title"), max_length=255, null=True, blank=True)
    icon = models.CharField(verbose_name=_("Left icon"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("Sgp Score")
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.title}-{self.description}"