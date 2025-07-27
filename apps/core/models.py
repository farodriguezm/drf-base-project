from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.indexes import GinIndex
from project_name.helpers import upload_to_uuid


class Log(models.Model):
    table = models.CharField(max_length=64)
    action = models.CharField(max_length=64)
    data = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Logs'
        indexes = [
            models.Index(fields=['table', 'action', 'user']),
            models.Index(fields=['created_at']),
            GinIndex(fields=['data'])
        ]

    def __str__(self):
        return f'{self.user.username} - {self.table} - {self.action} - {self.created_at}'


class Upload(models.Model):
    name = models.CharField(max_length=255)
    extension = models.CharField(max_length=10)
    size = models.PositiveBigIntegerField()
    file = models.FileField(upload_to=upload_to_uuid)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Uploads'
