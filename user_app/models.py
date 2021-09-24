from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    comment = models.CharField(max_length=512)
    profile_icon = models.ImageField(upload_to="profile_icons",blank=True, null=True)
    # file = models.FileField()
