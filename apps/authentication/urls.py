from dj_rest_auth.views import LoginView, LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ProfileView

app_name = 'authentication'

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
    path('profile', ProfileView.as_view(), name='profile'),
]
