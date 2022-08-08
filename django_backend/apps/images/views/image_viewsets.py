from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.base.permissions import IsOwnerImageOrReadOnly
from apps.images.models import Image
from apps.images.serializers.image_serializers import ImageSerializer


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# -------------------------------------------------------------
#                       Image view set
# -------------------------------------------------------------


class ImageViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerImageOrReadOnly,)
    queryset =  Image.objects.all()
    serializer_class = ImageSerializer
    filterset_fields = ['title']
