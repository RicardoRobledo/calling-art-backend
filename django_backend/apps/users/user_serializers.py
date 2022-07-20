from rest_framework import serializers

from .models import User


__author__ = "Ricardo"
__version__ = "0.1"


# -------------------------------------------------------------
#                       User serializer
# -------------------------------------------------------------


class UserSerializer(serializers.ModelSerializer):
    """
    This class seralize our User model
    """
    
    class Meta:
        """
        This inner class define our fields to show and our model to use
        
        Attributes:
            model (User): User instance to make reference
            field tuple(str): fields to show
        """
        
        model: User = User
        fields: tuple = ('username', 'email', 'description', 'icon',)
