from django.contrib.sessions.models import Session
from django.contrib.auth import login, logout
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from datetime import datetime

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
                user_serializer = UserTokenSerializer(user)
                
                login(request, user)

                message = {
                    'Token':token.key,
                    'User':user_serializer.data,
                }
                status_gotten = status.HTTP_200_OK

            else:

                message = {'message':'error debibo a que ese usuario no esta activo'},
                status_gotten = status.HTTP_401_UNAUTHORIZED

        else:

            message = {'message':'error en credenciales'}
            status_gotten = status.HTTP_401_UNAUTHORIZED

        return format_response(message, status_gotten)


# ---------------------------------------------
#                 Register view
# ---------------------------------------------


class RegisterView(APIView):


    def post(self, request, *args, **kwargs):
        """
        This method is for register our user

        Returns:
            Our response object formatted
        """
        
        register_serializer = UserSerializer(data=request.data)
        message = None
        status_gotten = None
        

        if register_serializer.is_valid():
            
            user = register_serializer.save()
            Token.objects.get_or_create(user=user)
            
            message = {'message':'usuario creado con exito'}
            status_gotten = status.HTTP_200_OK
            
        else:
            
            message = {'message':'ese usuario ya existe'}
            status_gotten = status.HTTP_400_BAD_REQUEST

        return format_response(message, status_gotten)


# ---------------------------------------------
#                 Logout view
# ---------------------------------------------


class LogoutView(APIView):


    def get(self, request, *args, **kwargs):
        """
        This method is for log out

        Returns:
            Our response object formatted
            
        Exception:
            IndexError: It will be generated if a header does not contain a token 
        """
        
        message = None
        status_gotten = None
        
        try:

            token_gotten = Token.objects.filter(
                            key=request.headers['Authorization'].split()[1]
                            )

            if token_gotten.exists():

                logout(request)
                token_gotten.delete()
                
                message = {
                    'message':'cierre de sesion exitoso'
                }
                status_gotten = status.HTTP_200_OK

            else:
                
                message = {
                    'message':'error debido a que el token de acceso proporcionado no se encuentra registrado'
                }
                status_gotten = status.HTTP_401_UNAUTHORIZED
        
        except IndexError:

            message = {
                    'message':'error debido a que no se ha proporcionado el token de acceso'
                }
            status_gotten = status.HTTP_400_BAD_REQUEST

        return format_response(message, status_gotten)
