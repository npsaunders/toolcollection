from django.contrib import admin

from .models import Maintenance, Storage, Tool

admin.site.register(Tool)
admin.site.register(Maintenance)
admin.site.register(Storage)