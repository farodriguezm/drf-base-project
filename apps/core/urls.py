from django.urls import path
from .views import UploadListView, UploadDetailView

app_name = 'core'

urlpatterns = [
    path('uploads', UploadListView.as_view(), name='upload-list'),
    path('uploads/<int:pk>', UploadDetailView.as_view(), name='upload-detail'),
]
