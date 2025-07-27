import uuid

from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class PageSizePagination(PageNumberPagination):
    page_size = settings.PAGE_SIZE
    page_size_query_param = 'page_size'


def upload_to_uuid(instance, filename, path='uploads'):
    ext = filename.rsplit('.', 1)[-1]
    return f'{path}/{uuid.uuid4()}.{ext}'
