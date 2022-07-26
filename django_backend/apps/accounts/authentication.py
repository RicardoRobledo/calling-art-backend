from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

from rest_framework.authtoken.models import Token


__author__ = 'Ricardo'
__version__ = '0.1'


# -------------------------------------------------
#             User token authentication
# -------------------------------------------------


class TokenAuthenticationManager():
    """
    This class manage a token expired to refresh it
    """

    def search_token(self, token):
        
        user = Token.objects.filter(key=token).first()
        
        if user:
            
            
            
            return user

        else:

            return None


    def refresh_token(self, token):
        pass


class UserTokenAuthentication(TokenAuthentication):
    """
    This class define our authentication with tokens
    
    Attributes:
        manager (TokenAuthenticationManager): object that handle tokens expired
        token (str): user's token
        user (User): user object 
    """


    manager = TokenAuthenticationManager()
    token = None
    user = None
    

    def authenticate(self, request):
        """
        This method verify that the token exists

        Raises:
            IndexError: tell us that our request does not contain a token 
        """
        
        try:

            token = request.headers['Authorization'].split()[1]

        except IndexError:
            raise exceptions.AuthenticationFailed('error, no se ha proporcionado el token')

        
        user = self.manager.search_token(token)
