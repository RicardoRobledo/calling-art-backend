from django.urls import path

from .views import LoginView


__author__ = 'Ricardo'
__version__ = '0.1'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login')
]
