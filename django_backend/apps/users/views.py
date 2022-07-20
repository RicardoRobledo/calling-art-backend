from rest_framework import viewsets

from apps.users.models import User
from apps.users.user_serializers import UserSerializer


__author__ = "Ricardo"
__version__ = "0.1"


# -------------------------------------------------------------
#                       User view set
# -------------------------------------------------------------


class UserViewSet(viewsets.ModelViewSet):
    """
    This class define our view abour an user

    Attributes:
        serializer_class (UserSerializer): Contains our serializer
        queryset (QuerySet): Contains our query of an user model
    """
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
