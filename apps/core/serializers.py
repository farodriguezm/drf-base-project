from django.conf import settings
from rest_framework import serializers
from .models import Upload
from rest_framework.exceptions import ValidationError


class UploadSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    extension = serializers.CharField(required=False)
    size = serializers.IntegerField(required=False)
    size_display = serializers.SerializerMethodField()

    class Meta:
        model = Upload
        fields = ['id', 'name', 'extension', 'size', 'size_display',
                  'file', 'created_at', 'updated_at']

    def validate(self, attrs):
        file = attrs.get('file')
        if not file:
            raise ValidationError({'message': 'File is required.'})

        extension = file.name.split('.')[-1].lower()
        if extension not in settings.ALLOWED_EXTENSIONS:
            raise ValidationError(
                {'message': f'File extension {extension} is not allowed.'})

        attrs['name'] = file.name
        attrs['extension'] = extension
        attrs['size'] = file.size
        return attrs

    def get_size_display(self, obj):
        return format_size(obj.size)


def format_size(size):
    if size < 1024:
        return f'{size} B'
    elif size < 1024 ** 2:
        return f'{size / 1024:.2f} KB'
    elif size < 1024 ** 3:
        return f'{size / (1024 ** 2):.2f} MB'
    else:
        return f'{size / (1024 ** 3):.2f} GB'
