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


    class CategoryChoice(models.TextChoices):
        """
        This inner class define our choices for several categories
    
        Attributes:
            VIDEOGAMES tuple(str): Choice for videogames.
            ANIME tuple(str): Choice for anime.
            MUSIC tuple(str): Choice for music.
            CARTOONS tuple(str): Choice for cartoons.
        """
        
        VIDEOGAMES = ('VIDEOGAMES', 'Videogames')
        ANIME = ('ANIME', 'Anime')
        MUSIC = ('MUSIC', 'Music')
        CARTOONS = ('CARTOONS', 'Cartoons')


    category = models.CharField(max_length=15, choices=CategoryChoice.choices, null=False, blank=False)
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
        user (int): id to reference an user
    """


    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    link = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='ImageCategory')


# -------------------------------------------------------------
#                       Image category
# -------------------------------------------------------------


class ImageCategory(models.Model):
    """
    This model define an image category

    Args:
        image (int): id to reference an image
        category (int): id to reference a category
    """


    image = models.ForeignKey(Image, null=False, blank=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
