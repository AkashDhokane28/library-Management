from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    mobile = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    is_user= models.BooleanField(default=False)
    address = models.TextField(max_length=999,null=True,blank=True)
    class Meta:
        db_table = 'user'