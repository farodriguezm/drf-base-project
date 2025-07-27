from django.contrib import admin
from .models import Log, Upload


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['table', 'action', 'user', 'data']


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['name', 'extension', 'size', 'file']
    list_filter = ['extension']
