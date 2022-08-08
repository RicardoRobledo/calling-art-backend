from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

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


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description='list our categories'
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description=':param category: category which belongs the image'
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description=':param id: primary key of category'
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="""
    :param id: primary key of category
    :param category: new category
    """
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description=':param id: primary key of category'
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description='partial_update'
))
class CategoryViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset =  Category.objects.all()
    serializer_class = CategorySerializer


# -------------------------------------------------------------
#                       ImageCategory view set
# -------------------------------------------------------------


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description='list our image categories'
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="""
    :param category: foreign key of category
    :param image: foreign key of image
    """
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description=':param id: primary key of an image category'
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="""
    :param id: primary key of an image category
    :param category: foreign key of category
    :param image: foreign key of image
    """
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description=':param id: primary key of an image category'
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description='partial_update'
))
class ImageCategoryViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset =  ImageCategory.objects.all()
    serializer_class = ImageCategorySerializer
