from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import(
    Category,
    ImageCategory,
)
from ..serializers.general_serializers import (
    CategorySerializer,
    ImageCategorySerializer,
)


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# -------------------------------------------------------------
#                       Category view set
# -------------------------------------------------------------


class CategoryViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset =  Category.objects.all()
    serializer_class = CategorySerializer


# -------------------------------------------------------------
#                       ImageCategory view set
# -------------------------------------------------------------


class ImageCategoryViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset =  ImageCategory.objects.all()
    serializer_class = ImageCategorySerializer
