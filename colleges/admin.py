""" modeladmins """

from django.contrib import admin
from .models import College, Branch

admin.site.register(College)
admin.site.register(Branch)
