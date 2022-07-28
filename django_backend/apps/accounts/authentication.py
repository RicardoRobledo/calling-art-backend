from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.conf import settings


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

                token_validated = self.refresh_token(token_validated)
                
            return token_validated.user

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

        
        if(time.year>token_created.year or
           time.month>token_created.month or
           time.day>token_created.day):
            return True

        if actual_minute<token_creation_minute:
            past_minutes = 60-token_creation_minute+actual_minute            
        else:
            past_minutes = actual_minute-token_creation_minute

        if past_minutes>=settings.TOKEN_EXPIRATION_TIME:
            return True

        return False


    def refresh_token(self, token:Token):
        """
        This method replace our old token by a new one
        
        Args:
            token (Token): token object expired
        
        Returns:
            An token object with an updated key
        """
        
        user = token.user
        token.delete()

        return Token.objects.select_related('user').get_or_create(user=user)[0]


class UserAuthenticationManager():
    """
    This class manage a user to authenticate it 
    """
    pass


class UserTokenAuthentication(TokenAuthentication):
    """
    This class define our authentication with tokens
    
    Attributes:
        token_manager (TokenAuthenticationManager): object to manage our token authentication
        user_manager (UserAuthenticationManager): object to manage our user authentication
    """


    token_manager = TokenAuthenticationManager()
    user_manager = UserAuthenticationManager()


    def authenticate(self, request):
        """
        This method verify that a token is received

        Raises:
            IndexError: tell us that our request does not contain a token 
        """
        
        token = None

        try:

            token = request.headers['Authorization'].split()[1]
        
        except IndexError:
        
            raise exceptions.AuthenticationFailed('error, no se ha proporcionado el token')
        
        except KeyError:
            
            body = request.body.decode().split()
            user = body[4]
            password = body[9]
            
            return self.authenticate_user(user, password)

        return self.authenticate_credentials(token)


    def authenticate_credentials(self, token:Token) -> tuple:
        """
        This method verify that the token exists and user is active
        
        Args:
            token (Token): token object to verify

        Raises:
            AuthenticationFailed: tell us that happend one of these 2 things
                1.- The given token does not exists
                2.- The user is not active
        """
        
        user = self.token_manager.search_token(token)
        
        if not user is None:

            if not user.is_active:
                raise exceptions.AuthenticationFailed('error, el usuario no esta activo')

            return (user, token)
            
        else:
            raise exceptions.AuthenticationFailed('error, el token proporcionado no existe')


    def authenticate_user(self, user:str, password:str):
        """
        This method verify that the token exists and user is active
        
        Args:
            user (str): user to verify is exists
            password (str): password to verify if exists

        Raises:
            AuthenticationFailed: tell us that happend one of these 2 things
                1.- The given token does not exists
                2.- The user is not active
        """
        
        pass
    