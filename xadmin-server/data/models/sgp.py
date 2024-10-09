from django.db import models
from django.utils.translation import gettext_lazy as _

from common.core.models import DbAuditModel, DbUuidModel


class SgpScore(models.Model):
    sgp考试科目 = models.IntegerField(blank=True, null=True)
    sgp人员 = models.IntegerField(blank=True, null=True)
    sgp成绩 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_sgpscore'

    # class Meta:
    #     verbose_name = _("Sgp Score")
    #     verbose_name_plural = verbose_name

    # def __str__(self):
    #     return f"{self.name}({self.code})"
