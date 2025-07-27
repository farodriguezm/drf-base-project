from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Profile
from .serializers import ProfileSerializer
from ..core.mixins import LogMixin


class ProfileView(LogMixin, RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        profile = Profile.objects.filter(user=self.request.user).first()
        if not profile:
            raise ValidationError({'message': 'Profile not found'})
        return profile

    def perform_update(self, serializer):
        with transaction.atomic():
            old = self.serializer_class(self.get_object()).data
            serializer.save()
            self.save_log('profile', 'update', {
                'old': old, 'new': serializer.data
            })
