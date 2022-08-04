from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.users.models import User
from apps.users.user_serializers import UserSerializer
from apps.base.permissions import IsOwnerUserOrReadOnly


__author__ = "Ricardo"
__version__ = "0.1"


# -------------------------------------------------------------
#                       User view set
# -------------------------------------------------------------


class UserViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerUserOrReadOnly,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
