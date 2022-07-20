from rest_framework import viewsets

from apps.images.models import Image
from apps.images.serializers.image_serializers import ImageSerializer


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# -------------------------------------------------------------
#                       Image view set
# -------------------------------------------------------------


class ImageViewSet(viewsets.ModelViewSet):
    
    queryset =  Image.objects.all()
    serializer_class = ImageSerializer
