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
    
    email = models.EmailField(unique=True, null=False, blank=False,)
    username = models.CharField(max_length=20, null=False, blank=False,)
    description = models.CharField(max_length=200, null=False, blank=False,)
    icon = models.CharField(max_length=200, null=False, blank=False,)
    created_at = models.DateTimeField(auto_now_add=True)


# -------------------------------------------------------------
#                           Category
# -------------------------------------------------------------
class Category(models.Model):
    """
    This model define a category

    Args:
        category (datetime): creation date
        created_at (str): description of the image
    """
    
    category = models.CharField(max_length=15, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


# -------------------------------------------------------------
#                             Image
# -------------------------------------------------------------
class Image(models.Model):
    """
    This model define an Image

    Args:
        title (str): title of the image
        description (str): description of the image
        link (str): url of the image
        created_at (datetime): creation date
        id_user (int): id to reference an user
    """
    
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    link = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    id_user = models.ManyToManyField(User, null=False, blank=False, through='ImageCategory', on_delete=models.CASCADE)


# -------------------------------------------------------------
#                       Image category
# -------------------------------------------------------------
class ImageCategory(models.Model):
    """
    This model define an image category

    Args:
        id_image (int): id to reference an image
        id_category (int): id to reference a category
    """
    
    id_image = models.ForeignKey(Image, null=False, blank=False, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)