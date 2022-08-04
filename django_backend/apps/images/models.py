from django.db import models


__author__ = 'Ricardo'
__version__ = '0.1'


# -------------------------------------------------------------
#                           Category
# -------------------------------------------------------------


class Category(models.Model):
    """
    This model define a category

    Attributes:
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

    Attributes:
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
    user = models.ForeignKey('users.User', null=False, blank=False, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='ImageCategory')


# -------------------------------------------------------------
#                       Image category
# -------------------------------------------------------------


class ImageCategory(models.Model):
    """
    This model define an image category

    Attributes:
        image (int): id to reference an image
        category (int): id to reference a category
    """


    image = models.ForeignKey(Image, null=False, blank=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
