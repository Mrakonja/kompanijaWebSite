from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_photo = models.ImageField()
    title = models.CharField(max_length=50)
    is_team_member = models.BooleanField()
    is_test_user = models.BooleanField()
    email = models.EmailField()
    account = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name="user auth",)