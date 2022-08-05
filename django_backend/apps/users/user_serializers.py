from rest_framework import serializers

from .models import User


__author__ = "Ricardo"
__version__ = "0.1"


# -------------------------------------------------------------
#                       User serializer
# -------------------------------------------------------------


class UserTokenSerializer(serializers.ModelSerializer):
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
        """
        This method return us our json representation
        """
        
        images: list = [
            {
                image.title :{
                    'id': image.id,
                    'description': image.description,
                    'link': image.link,
                }
            }
            for image in self.Meta.model.objects.get(id=instance.id).image_set.all()
        ]

        return {
            'id': instance.id,
            'username': instance.username,
            #'password': instance.password,
            'email': instance.email,
            'description': instance.description,
            'icon': instance.icon,
            'created_at': instance.created_at,
            'images': images, 
        }


    def create(self, validated_data) -> User:
        """
        This method create our user

        Args:
            validated_data (dict): data dict our validated instance 

        Returns:
            Our user validated with encrypted password
        """

        user_validated = User(**validated_data)
        user_validated = self.encript_password(user_validated, validated_data['password'])
        user_validated.save()
        
        return user_validated


    def update(self, instance, validated_data) -> User:
        """
        This method update our user

        Args:
            instance (User): user object
            validated_data (dict): dict with our new values to add

        Returns:
            Our user validated with encrypted password
        """
        
        user_validated = super().update(
            instance=instance,
            validated_data=validated_data
        )
        user_validated = self.encript_password(user_validated, validated_data['password'])
        user_validated.save()

        return user_validated
    
    
    def encript_password(self, user_validated:User, password:str) -> User:
        """
        This method encript the password to an user

        Args:
            user_validated (User): user object updated
            password (str): password to encript

        Returns:
            A user instance with encripted password
        """
        
        user_validated.set_password(password)
        
        return user_validated
