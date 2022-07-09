from rest_framework import viewsets
from .models import(
    User,
    Category,
    Image,
    ImageCategory,
)
from .serializers import (
    UserSerializer,
    CategorySerializer,
    ImageSerializer,
    ImageCategorySerializer,
)


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# -------------------------------------------------------------
#                         User view set
# -------------------------------------------------------------


class UserViewSet(viewsets.ModelViewSet):
    
    queryset =  User.objects.all()
    serializer_class = UserSerializer


# -------------------------------------------------------------
#                       Category view set
# -------------------------------------------------------------


class CategoryViewSet(viewsets.ModelViewSet):
    
    queryset =  Category.objects.all()
    serializer_class = CategorySerializer


# -------------------------------------------------------------
#                       Image view set
# -------------------------------------------------------------


class ImageViewSet(viewsets.ModelViewSet):
    
    queryset =  Image.objects.all()
    serializer_class = ImageSerializer


# -------------------------------------------------------------
#                       Image view set
# -------------------------------------------------------------


class ImageCategoryViewSet(viewsets.ModelViewSet):
    
    queryset =  ImageCategory.objects.all()
    serializer_class = ImageCategorySerializer
