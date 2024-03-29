from rest_framework import serializers

from apps.users.models import User
from ..models import Image, ImageCategory


__author__ = "Ricardo Robledo"
__version__ = "0.1"


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
        fields: tuple = ('id', 'title', 'link', 'description', 'created_at', 'user',)


    def to_representation(self, instance):
        """
        This method return us our Json representation
        """

        categories: list = [
            imagecategory.category.category
            for imagecategory in ImageCategory.objects.filter(image=instance.id)
        ]

        return {
            'id': instance.id,
            'user_id': instance.user.id,
            'title': instance.title,
            'description': instance.description,
            'link': instance.link,
            'created_at': instance.created_at,
            'categories': categories,
        }


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
    
    
    def update(self, instance, validated_data) -> Image:
        """
        This method update our image

        Args:
            instance (Image): image object
            validated_data (dict): dict with our new values to add

        Returns:
            Our image validated
        """

        validated_data['user'] = User.objects.get(id=validated_data['user']['id'])

        # This is for set each value in each key that contains both
        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        instance.save()

        return instance
