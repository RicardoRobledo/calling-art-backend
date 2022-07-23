from rest_framework import serializers

from apps.users.models import User


__author__ = 'Ricardo'
__version__ = '0.1'


class UserTokenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'username':instance.username,
            'email':instance.email,
            'description':instance.description,
            'icon':instance.icon,
        }
    
