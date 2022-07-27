from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.conf import settings
from datetime import timedelta


__author__ = 'Ricardo'
__version__ = '0.1'


# -------------------------------------------------
#             User token authentication
# -------------------------------------------------


class TokenAuthenticationManager():
    """
    This class manage a token expired to refresh it

    Attributes:
        token (Token): Token object
    """


    def __init__(self):
        self.__token:Token = None


    @property
    def token(self) -> Token:
        return self.__token
    
    
    @token.setter
    def token(self, token:Token) -> None:
        self.__token = token


    def search_token(self, token:str):
        """
        This method look for an user with a specific token
        
        Agrs:
            token (str): contains a token in string format

        Returns:
            An user found
        """
        
        token_validated = Token.objects.select_related('user').filter(key=token).first()
        
        # case 1: token exists
        if token_validated:

            # case 2: token is expired
            if self.is_expired(token_validated):
                
                self.refresh_token()
                print("Expirado")
            
            else:
                
                print("No expirado")

            return token_validated

        else:

            return None


    def is_expired(self, token:Token) -> bool:
        """
        This method verify wether if a token given is expired
        
        Args:
            token (Token): Token object found
        
        Returns:
            A boolean that tell us if a token is expired
        """

        token_created = token.created
        time = timezone.now()
        actual_minute = time.minute
        token_creation_minute = token_created.minute
        past_minutes = None


        if actual_minute<token_creation_minute:
            past_minutes = 60-token_creation_minute+actual_minute            
        else:
            past_minutes = actual_minute-token_creation_minute

        if past_minutes>=settings.TOKEN_EXPIRATION_TIME:
            return True

        return False


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
        
        token = None

        try:

            token = request.headers['Authorization'].split()[1]

        except IndexError:

            raise exceptions.AuthenticationFailed('error, no se ha proporcionado el token')

        user = self.manager.search_token(token)
        
        if not user is None:
        
            print('Si')
        
        else:
        
            print('No')
    