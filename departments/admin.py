""" modeladmins """

from django.contrib import admin
from .models import Department, HOD

admin.site.register(Department)
admin.site.register(HOD)
