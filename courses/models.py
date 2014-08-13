""" Course Models """

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Course(models.Model):
    """
    Course:
        name: Course Name
        code: Course Code.
    """
    name = models.CharField(_("Course Name"),
                            max_length=120)
    code = models.CharField(_("Course Code"),
                            max_length=10)
    department = models.ForeignKey("departments.Department")

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return self.name + " - " + self.code


class CourseInstructor(models.Model):
    """
    Course Instructor:
        course: ForeignKey to Course
        instructor: ForeignKey to Faculty
    """
    course = models.ForeignKey("courses.Course")
    instructor = models.ForeignKey("faculties.Faculty")
    from_time = models.DateTimeField(blank=True,
                                     null=True)
    to_time = models.DateTimeField(blank=True,
                                   null=True)

    class Meta:
        verbose_name = _('Course Instructor')
        verbose_name_plural = _('Course Instructors')

    def __str__(self):
        return self.course.name + " - " + self.instructor.user.get_full_name()


class CourseCalender(models.Model):
    """
    CourseCalender:
        course: ForeignKey to Course
        instructor: ForeignKey to instructor
    """

    course = models.ManyToManyField("courses.Course")
    from_time = models.DateTimeField(blank=True,
                                     null=True)
    to_time = models.DateTimeField(blank=True,
                                   null=True)

    class Meta:
        verbose_name = _('Course Calender')
        verbose_name_plural = _('Course Calenders')

    def __str__(self):
        return self.course.name


class Topic(models.Model):
    """ Topic Model """
    course = models.ForeignKey("courses.Course")
    name = models.CharField(_("Name"),
                            max_length=120)
    description = models.CharField(_("Description"),
                                   max_length=3000)

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')

    def __str__(self):
        return self.name
