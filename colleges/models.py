""" Models for 'colleges' app """

from django.db import models
from django.utils.translation import ugettext_lazy as _


class College(models.Model):
    """
    College:
        name: College Name
        code: College Code.
    """
    name = models.CharField(_("College Name"),
                            max_length=120)
    code = models.CharField(_("College Code"),
                            max_length=10)

    class Meta:
        verbose_name = _('College')
        verbose_name_plural = _('Colleges')

    def __str__(self):
        return self.name + " - " + self.code
