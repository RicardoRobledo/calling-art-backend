from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.base.utils import format_response
from apps.users.user_serializers import UserSerializer, UserTokenSerializer


# ---------------------------------------------
#                    Login view
# ---------------------------------------------


class LoginView(TokenObtainPairView):
    
    serializer_class = TokenObtainPairSerializer


    def post(self, request, *args, **kwargs):
        """
        This method is for do login

        Returns:
            Our response object formatted
        """
        
        login_serializer = self.serializer_class(data=request.data)
        message = None
        status_gotten = None


        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()


        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )

  
        if login_serializer.is_valid():

            user_token_serializer = UserTokenSerializer(user)
        
            login(request, user)

            message = {
                'user':user_token_serializer.data,
            }
            status_gotten = status.HTTP_200_OK

            response = format_response(message, status_gotten)
            response.set_cookie(key='jwt', value=login_serializer.validated_data)

            return response


        message = {
            'message':'error in type of data',
        }
        status_gotten = status.HTTP_401_UNAUTHORIZED

        return format_response(message, status_gotten)


# ---------------------------------------------
#                 Register view
# ---------------------------------------------


class RegisterView(APIView):
    
    permission_classes = ()


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
            
            message = {'message':'usuario creado con exito'}
            status_gotten = status.HTTP_201_CREATED
            
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

        #logout(request)
                
        message = {
            'message':'cierre de sesion exitoso'
        }
        status_gotten = status.HTTP_200_OK

        return format_response(message, status_gotten)
