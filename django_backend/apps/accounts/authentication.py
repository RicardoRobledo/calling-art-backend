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
    def token(self, token:str) -> None:
        self.__token = token


    def search_token(self):
        """
        This method look for an user with a specific token

        Returns:
            An user found
        """
        
        token_validated = Token.objects.select_related('user').filter(key=self.__token).first()
        
        # case 1: token exists
        if token_validated:
            
            # case 2: token is expired
            if self.is_expired():
                
                self.refresh_token()

            return token_validated

        else:

            return None


    def is_expired(self) -> bool:
        """
        This method verify wether if a token given is expired
        
        Returns:
            A boolean that tell us if a token is expired
        """
        
        self.__token
        
        return True


    def refresh_token(self):
        """
        This method replace our old token by a new one
        """
        pass


class UserTokenAuthentication(TokenAuthentication):
    """
    This class define our authentication with tokens
    """


    manager = TokenAuthenticationManager()


    def authenticate(self, request):
        """
        This method verify that the token exists

        Raises:
            IndexError: tell us that our request does not contain a token 
        """

        try:

            self.manager.token = request.headers['Authorization'].split()[1]

        except IndexError:

            raise exceptions.AuthenticationFailed('error, no se ha proporcionado el token')

        user = self.manager.search_token()
        
        if not user is None:
        
            print('Si')
        
        else:
        
            print('No')
    