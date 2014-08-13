""" Models for Faculty """

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Faculty(models.Model):

    """
    Faculty:
        user: ForeignKey to User Object
        disgnation: Faculty designation.
        qualification: Qualification
    """
    user = models.ForeignKey("auth.User")
    qualification = models.CharField(_("Qualification"),
                                     max_length=60)
    designation = models.CharField(_("Designation"),
                                   max_length=60)
    department = models.ForeignKey("departments.Department")

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculties')

    def __str__(self):
        return self.user.get_full_name() + " - " + self.designation
