from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='customuser_set',  # Add related_name to avoid conflicts
    #     blank=True,
    #     help_text=('The groups this user belongs to. A user will get all permissions '
    #                'granted to each of their groups.'),
    #     verbose_name=('groups')
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='customuser_set',  # Add related_name to avoid conflicts
    #     blank=True,
    #     help_text=('Specific permissions for this user.'),
    #     verbose_name=('user permissions')
    # )

    objects = UserManager()
