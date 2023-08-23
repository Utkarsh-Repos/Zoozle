from django.db import models
from django.contrib.auth.models import User


class UserPhone(models.Model):
    user_detail = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()