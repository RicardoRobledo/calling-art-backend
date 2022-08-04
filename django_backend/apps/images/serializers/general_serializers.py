"""
This module define our serializers
"""


from venv import create
from rest_framework import serializers

from ..models import(
    Category,
    Image,
    ImageCategory,
)


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# -------------------------------------------------------------
#                       Category serializer
# -------------------------------------------------------------


class CategorySerializer(serializers.ModelSerializer):
    """
    This class serialize our category model
    """


    class Meta:
        """
        This inner class define our fields to show and our model to use
        
        Attributes:
            model (Category): category instance to make reference
            field tuple(str): fields to show
        """


        model: Category = Category
        fields: tuple = ('category', 'created_at',)


# -------------------------------------------------------------
#                   Image category serializer
# -------------------------------------------------------------


class ImageCategorySerializer(serializers.ModelSerializer):
    """
    This class serialize our image category model
    
    Attributes:
        category (PrimaryKeyRelatedField): related categories to select
        image (int): integer of a image's foreign key 
    """


    #category = CategorySerializer()
    category: int = serializers.IntegerField(source="category.id")
    image: int = serializers.IntegerField(source="image.id")


    class Meta:
        """
        This inner class define our fields to show and our model to use
        
        Attributes:
            model (ImageCategory): image category instance to make reference
            field tuple(str): fields to show
        """


        model: ImageCategory = ImageCategory
        fields: str = '__all__'


    def create(self, validated_data: dict) -> ImageCategory:
        """
        This method search an image with his id to place it in an image category's information
        to make an image category up

        Args:
            validated_data (dict): dictionary with an image's information

        Returns:
            An image category instance
        """


        validated_data['category'] = Category.objects.get(id=validated_data['category']['id'])
        validated_data['image'] = Image.objects.get(id=validated_data['image']['id'])
        
        return ImageCategory.objects.create(**validated_data)
