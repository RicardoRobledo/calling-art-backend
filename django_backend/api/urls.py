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
router.register('user/', UserViewSet.as_view(), basename='user')
router.register('category/', CategoryViewSet.as_view(), basename='category')
router.register('image-category/', ImageCategoryViewSet.as_view(), basename='image-category')
router.register('', ImageViewSet.as_view(), basename='image')

urlpatterns = router.urls
