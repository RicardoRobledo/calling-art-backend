from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.base.utils import format_response
from apps.users.models import User
from apps.users.user_serializers import UserSerializer
from apps.accounts.serializers import CustomTokenObtainPairSerializer


# ---------------------------------------------
#         Custom Token Obtain Pair View
# ---------------------------------------------


class CustomTokenObtainPairView(TokenObtainPairView):

    serializer_class = CustomTokenObtainPairSerializer


# ---------------------------------------------
#                    Login view
# ---------------------------------------------


class LoginView(TokenObtainPairView):
    
    serializer_class = CustomTokenObtainPairSerializer


    def post(self, request, *args, **kwargs):
        """
        Allow us login and get a cookie with our access tokens
        
        :param username: username of our user
        :param password: password of our user
        :returns: a Response object with a cookie
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
        
            login(request, user)
            status_gotten = status.HTTP_200_OK

            return format_response(login_serializer.validated_data, status_gotten)


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
        Allow us sign up
        
        :param username: username of our user
        :param password: password of our user
        :param email: email of our user
        :param description: a description of our user
        :param icon: icon to show the user 
        :returns: a response object
        """

        message = None
        status_gotten = None
        register_serializer = UserSerializer(data=request.data)
        
        user = User.objects.filter(username=request.data['username']).exists()
        email = User.objects.filter(email=request.data['email']).exists()


        if user:

            message = {'message':'that user already exists'}
            status_gotten = status.HTTP_400_BAD_REQUEST
        
        elif email:
        
            message = {'message':'that email already exists'}
            status_gotten = status.HTTP_400_BAD_REQUEST
        
        elif register_serializer.is_valid():

            register_serializer.save()

            message = {'message':'user created'}
            status_gotten = status.HTTP_201_CREATED
            
        else:
            
            message = {'message':'wrong record'}
            status_gotten = status.HTTP_400_BAD_REQUEST

        return format_response(message, status_gotten)


# ---------------------------------------------
#                 Logout view
# ---------------------------------------------


class LogoutView(APIView):


    def get(self, request, *args, **kwargs):
        """
        Allow us logout
        
        :param username: username
        """
        
        message = None
        status_gotten = None

        
        user = User.objects.filter(username=request.data.get('username'))


        if user.exists():

            #RefreshToken.for_user(user.first())
            logout(request)

            message = {
                'message':'logout success'
            }
            status_gotten = status.HTTP_200_OK

            response = format_response(message, status_gotten)
            response.delete_cookie(settings.COOKIE_NAME)

            return response


        message = {
            'message':'error that user does not exists'
        }
        status_gotten = status.HTTP_401_UNAUTHORIZED

        return format_response(message, status_gotten)
