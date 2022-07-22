from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.authtoken.models import Token

from apps.base.utils import format_response
from apps.users.models import User


# ---------------------------------------------
#                    Login view
# ---------------------------------------------


class LoginView(ObtainAuthToken):


    def get(self, request, *args, **kwargs):
        """
        This method is for do login

        Returns:
            Our response object formatted
        """
        
        login_serializer = self.serializer_class(data=request.data)

        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            print(user)
            print(User.objects.all())
            
            return format_response(
                {'message':'Se ha iniciado sesion'},
                status.HTTP_200_OK
            )

        else:

            return format_response(
                {'message':'Error en credenciales'},
                status.HTTP_401_UNAUTHORIZED
            )
