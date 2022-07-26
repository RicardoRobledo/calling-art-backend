from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions


__author__ = 'Ricardo'
__version__ = '0.1'


# -------------------------------------------------
#             User token authentication
# -------------------------------------------------


class TokenAuthenticationManager:
    """
    This class manage a token expired to refresh it
    """

    def refresh_token(self, token):
        pass


class UserTokenAuthentication(TokenAuthentication):
    """
    This class define our authentication with tokens
    
    Attributes:
        manager (TokenAuthenticationManager): object that handle tokens expired
    """    

    manager = TokenAuthenticationManager()

    def authenticate(self, request):
        """
        This method verify that the token exists
        """
        pass
