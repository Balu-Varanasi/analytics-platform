""" Models for 'colleges' app """

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Department(models.Model):
    name = models.CharField(_("Department Name"),
                            max_length=120)
    code = models.CharField(_("Department Code"),
                            max_length=10)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def __str__(self):
        return self.name + " " + self.code
