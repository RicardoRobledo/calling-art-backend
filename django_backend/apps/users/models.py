from django.db import models
from django.contrib.auth.models import AbstractBaseUser


__author__ = 'Ricardo'
__version__ = '0.1'


# -------------------------------------------------------------
#                             User
# -------------------------------------------------------------


class User(AbstractBaseUser):
    """
    This model define an user

    Attributes:
        email (str): email of the user
        username (str): username of the user
        description (str): description of the user
        icon (str): url of the icon
        created_at (datetime): creation date
    """
    
    USERNAME_FIELD = 'username'

    email = models.EmailField(unique=True, null=False, blank=False,)
    username = models.CharField(unique=True, max_length=20, null=False, blank=False,)
    description = models.CharField(max_length=200, null=False, blank=False,)
    icon = models.CharField(max_length=200, null=False, blank=False,)
    created_at = models.DateTimeField(auto_now_add=True)
