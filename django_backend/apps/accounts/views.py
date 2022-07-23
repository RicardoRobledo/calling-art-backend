from django.urls import is_valid_path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token

from apps.base.utils import format_response
from apps.accounts.serializers import UserTokenSerializer
from apps.users.user_serializers import UserSerializer


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
        message = None
        status_gotten = None

        # case 1: data are valid
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            
            # case 2: user is active
            if user.is_active:
                
                token = Token.objects.get_or_create(user=user)[0]
                user = UserTokenSerializer(user)

                message = {
                    'Token':token.key,
                    'User':user.data,
                }
                status_gotten = status.HTTP_200_OK

            else:
                message = {'message':'Error debibo a que ese usuario no esta activo'},
                status_gotten = status.HTTP_401_UNAUTHORIZED

        else:

            message = {'message':'Error en credenciales'}
            status_gotten = status.HTTP_401_UNAUTHORIZED

        return format_response(message, status_gotten)


# ---------------------------------------------
#                 Register view
# ---------------------------------------------


class RegisterView(APIView):


    def post(self, request, *args, **kwargs):
        """
        This method is for do login

        Returns:
            Our response object formatted
        """
        
        register_serializer = UserSerializer(data=request.data)
        message = None
        status_gotten = None


        # si es valido
        if register_serializer.is_valid():
            
            user = register_serializer.save()
            Token.objects.get_or_create(user=user)
            
            message = {'message':'usuario creado con exito'}
            status_gotten = status.HTTP_200_OK
            
        else:
            
            message = {'message':'entrada de datos invalida'}
            status_gotten = status.HTTP_400_BAD_REQUEST
            

        return format_response(message, status_gotten)
