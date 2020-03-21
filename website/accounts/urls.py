from django.urls import path
from .views import ProfileView, LoginView, SignupView

urlpatterns = [
    path('profilе/<int:id>', ProfileView.as_view(), name='profile'),
    path('login', LoginView.as_view(), name='login'),
    ]