from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


__author__ = 'Ricardo'
__version__ = '0.1'


# -------------------------------------------------------------
#                             User
# -------------------------------------------------------------


class UserManager(BaseUserManager):


    def create_user(self, username, password, email, is_staff, is_active, is_superuser=False):
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, password, email):
        return self.create_user(username, password, email, True, True, True)


class User(AbstractBaseUser, PermissionsMixin):
    """
    This model define an user

    Attributes:
        email (str): email of the user
        username (str): username of the user
        description (str): description of the user
        icon (str): url of the icon
        created_at (datetime): creation date
    """
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()
    email = models.EmailField(unique=True, null=False, blank=False,)
    username = models.CharField(unique=True, max_length=20, null=False, blank=False,)
    description = models.CharField(max_length=200, null=False, blank=False,)
    icon = models.CharField(max_length=200, null=False, blank=False,)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
