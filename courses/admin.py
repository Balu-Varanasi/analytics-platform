from django.contrib import admin
from .models import Course, CourseCalender, CourseInstructor, Topic

admin.site.register(Course)
admin.site.register(CourseInstructor)
admin.site.register(CourseCalender)
admin.site.register(Topic)
