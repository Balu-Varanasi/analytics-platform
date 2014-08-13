""" Models for 'departments' app """

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Department(models.Model):
    """ Department Model """

    name = models.CharField(_("Name"),
                            max_length=120)
    code = models.CharField(_("Code"),
                            max_length=10)
    college = models.ForeignKey("colleges.College")
    hod = models.ForeignKey("departments.HOD")

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def __str__(self):
        return self.name + " - " + self.code


class HOD(models.Model):
    """ Head of the Department Model """

    faculty = models.ForeignKey("faculty.Faculty")

    class Meta:
        verbose_name = _('HOD')
        verbose_name_plural = _('HODs')

    def __str__(self):
        return self.faculty.user.get_full_name()
