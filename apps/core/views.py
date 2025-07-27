from django.db import transaction
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .mixins import LogMixin
from .models import Upload
from .serializers import UploadSerializer


class UploadListView(LogMixin, ListCreateAPIView):
    queryset = Upload.objects.all().order_by('id')
    serializer_class = UploadSerializer
    search_fields = ['name']

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()
            self.save_log('upload', 'create', serializer.data)


class UploadDetailView(LogMixin, RetrieveUpdateDestroyAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

    def perform_update(self, serializer):
        with transaction.atomic():
            old = self.serializer_class(self.get_object()).data
            serializer.save()
            self.save_log('upload', 'update', {
                          'old': old, 'new': serializer.data})

    def perform_destroy(self, instance):
        with transaction.atomic():
            data = self.serializer_class(self.get_object()).data
            instance.delete()
            self.save_log('upload', 'delete', data)
