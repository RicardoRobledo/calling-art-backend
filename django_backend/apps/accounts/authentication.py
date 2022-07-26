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


    def __init__(self):
        self.__token:str = None
        
    
    @property
    def token(self) -> str:
        return self.__token
    
    
    @token.setter
    def token(self, token) -> None:
        self.__token = token


    def search_token(self):
        
        user = Token.objects.filter(key=self.__token).first()
        
        if user:
            
            
            
            return user

        else:

            return None


    def is_expired(self):
        pass


    def refresh_token(self):
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

            self.token = request.headers['Authorization'].split()[1]

        except IndexError:
            raise exceptions.AuthenticationFailed('error, no se ha proporcionado el token')

        self.user = self.manager.search_token()
