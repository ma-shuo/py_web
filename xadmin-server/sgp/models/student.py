from django.db import models
from django.utils.translation import gettext_lazy as _
from common.core.models import DbSgpBaseModel


class Student(DbSgpBaseModel):
    student_name = models.CharField(verbose_name=_("姓名"), max_length=255, null=True, blank=True)
    school_issued_student_id = models.CharField(verbose_name=_("学号"), max_length=255, null=True, blank=True)
    provincial_issued_student_id = models.CharField(verbose_name=_("省学籍号"), max_length=255, null=True, blank=True)
    national_issued_student_id = models.CharField(verbose_name=_("国家学籍号"), max_length=255, null=True, blank=True)
    identity_card_number = models.CharField(verbose_name=_("身份证号"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = verbose_name
        ordering = ("-created_time",)

    def __str__(self):
        return f"{self.student_name}"