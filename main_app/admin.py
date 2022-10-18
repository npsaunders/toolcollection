from django.contrib import admin

from .models import Maintenance, Tool

admin.site.register(Tool)
admin.site.register(Maintenance)