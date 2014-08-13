""" Models for Students """

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):

    """
    Student:
        user: ForeignKey to User object
        registration number: Registration/Roll Number.
        course: Course Name
    """

    user = models.ForeignKey("auth.User")
    registration_number = models.CharField(_("Registration Number"),
                                           max_length=10)
    department = models.ForeignKey("departments.Department")

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __str__(self):
        return self.user.get_full_name() + " - " + self.registration_number
