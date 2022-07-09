"""
This module define our serializers
"""


from rest_framework import serializers
from .models import(
    User,
    Category,
    Image,
    ImageCategory,
)


__author__ = "Ricardo Robledo"
__version__ = "0.1"


# -------------------------------------------------------------
#                         User serializer
# -------------------------------------------------------------


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'description', 'icon', 'created_at',)


# -------------------------------------------------------------
#                       Category serializer
# -------------------------------------------------------------


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('category', 'created_at',)


# -------------------------------------------------------------
#                       Image serializer
# -------------------------------------------------------------


class ImageSerializer(serializers.ModelSerializer):
    
    user = serializers.IntegerField(source="user.id")    

    class Meta:
        model = Image
        fields = ('id', 'title', 'link', 'description', 'created_at', 'user')

    # This method save our updated model with the user stablished
    def create(self, validated_data):
        validated_data['user'] = User.objects.get(id=validated_data['user']['id']) # search user and replace in Python's dict
        return Image.objects.create(**validated_data)


# -------------------------------------------------------------
#                   Image category serializer
# -------------------------------------------------------------


class ImageCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ImageCategory
        fields = ('image', 'category',)
