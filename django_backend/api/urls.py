"""
This module define our paths through urls
"""


from django.urls import path
from .views import(
    UserViewSet,
    CategoryViewSet,
    ImageViewSet,
    ImageCategoryViewSet,
)
from rest_framework.routers import SimpleRouter


__author__ = 'Ricardo'
__version__ = '0.1'


router = SimpleRouter()
router.register('user', UserViewSet, basename='user')
router.register('category', CategoryViewSet, basename='category')
router.register('image-category', ImageCategoryViewSet, basename='image-category')
router.register('', ImageViewSet, basename='image')

urlpatterns = router.urls
