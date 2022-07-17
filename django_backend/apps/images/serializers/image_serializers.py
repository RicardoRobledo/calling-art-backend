from venv import create
from rest_framework import serializers

from apps.users.models import User
from ..models import Image


# -------------------------------------------------------------
#                       Image serializer
# -------------------------------------------------------------


class ImageSerializer(serializers.ModelSerializer):
    """
    This class serialize our image model
    
    Attributes:
        user (int): integer of a user's foreign key 
    """


    user: int = serializers.IntegerField(source="user.id")    


    class Meta:
        """
        This inner class define our fields to show and our model to use
        
        Attributes:
            model (Image): image instance to make reference
            field tuple(str): fields to show
        """
        
        model: Image = Image
        fields: tuple(str) = ('id', 'title', 'link', 'description', 'created_at', 'user')


    # This method save our updated model with the user stablished
    def create(self, validated_data:dict) -> Image:
        """
        This method search an user with his id to place him in an image's information
        to make an image up

        Args:
            validated_data (dict): dictionary with an image's information

        Returns:
            An image instance after create this one
        """


        validated_data['user'] = User.objects.get(id=validated_data['user']['id']) # search user and replace in Python's dict
        return Image.objects.create(**validated_data)
