from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

class CustomUserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields["role"] = "admin"
        return super().create_superuser(username, email, password, **extra_fields)

class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    objects = CustomUserManager()

    class Meta:
        db_table = 'auth_user'

