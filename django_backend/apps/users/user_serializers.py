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
        fields: tuple = ('username', 'password', 'email', 'description', 'icon',)


    def to_representation(self, instance):
        return {
            'username': instance.username,
            'email': instance.email,
            'description': instance.description,
            'icon': instance.icon,
            'created_at': instance.created_at,
        }


    def create(self, validated_data) -> User:
        """
        This method create our user

        Args:
            validated_data (dict): dict of our validated instance 

        Returns:
            Our user validated like encrypted password
        """

        user_validated = User(**validated_data)
        user_validated.set_password(validated_data['password'])
        user_validated.save()
        
        return user_validated
