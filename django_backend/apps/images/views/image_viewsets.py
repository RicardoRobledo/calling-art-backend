from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from apps.base.permissions import IsOwnerImageOrReadOnly
from apps.images.models import Image
from apps.images.serializers.image_serializers import ImageSerializer


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# -------------------------------------------------------------
#                       Image view set
# -------------------------------------------------------------


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description=':param title: image title'
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="""
    :param title: category which belongs the image
    :param link: image url
    :param description: brief description about a user
    :param user: user's foreign key
    """
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description=':param id: primary key of image'
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="""
    :param id: primaky key of image
    :param title: category which belongs the image
    :param link: image url
    :param description: brief description about a user
    :param user: user's foreign key
    """
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description=':param id: primaky key of image'
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description='partial_update'
))
class ImageViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerImageOrReadOnly,)
    queryset =  Image.objects.all()
    serializer_class = ImageSerializer
    filterset_fields = ['title']
