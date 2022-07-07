from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# -------------------------------------------------------------
#                             User
# -------------------------------------------------------------
class User(AbstractBaseUser):
    
    email = models.EmailField(unique=True, null=False, blank=False,)
    username = models.CharField(max_length=20, null=False, blank=False,)
    description = models.CharField(max_length=200, null=False, blank=False,)
    icon = models.CharField(max_length=200, null=False, blank=False,)
    created_at = models.DateTimeField(auto_now_add=True)


# -------------------------------------------------------------
#                             Image
# -------------------------------------------------------------
class Image(models.Model):
    
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    link = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
