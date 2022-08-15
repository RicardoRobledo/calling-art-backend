from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
import django_filters

from apps.base.paginations import CustomPagination
from apps.users.models import User
from apps.users.user_serializers import UserSerializer
from apps.base.permissions import IsOwnerUserOrReadOnly


__author__ = "Ricardo"
__version__ = "0.1"


# -------------------------------------------------------------
#                       User view set
# -------------------------------------------------------------


class UserFilter(django_filters.FilterSet):
    """
    This class filter our users by username and creation date

    Attributes:
        created_ate (datetime): creation date
        username (str): username
    """

    created_at = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    username = django_filters.CharFilter(field_name='username')
    
    class Meta:
        model = User
        fields = [
            'created_at',
            'username',
        ]


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="""
    :param username: username of our user
    :param created_at: creation date
    """
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description=""" 
    :param username: username of our user
    :param password: password of our user
    :param email: email of our user
    :param description: a description of our user
    :param icon: icon to show the user 
    """
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description=':param id: primary key of an user'
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="""
    :param username: username of our user
    :param password: password of our user
    :param email: email of our user
    :param description: a description of our user
    :param icon: icon to show the user
    :param id: primary key of an user
    """
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description='partial_update'
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description=':param id: primary key of an user'
))
class UserViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerUserOrReadOnly,)
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    filterset_class = UserFilter
    pagination_class = CustomPagination
    #filterset_fields = ['username']
    #filter_backends = [filters.SearchFilter]
