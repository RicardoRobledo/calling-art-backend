from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.images.views.image_viewsets import ImageViewSet
from apps.images.views.general_views import CategoryViewSet, ImageCategoryViewSet


__author__ = "Ricardo"
__version__ = "0.1"


router = SimpleRouter()
router.register('images', ImageViewSet, basename='images')
router.register('categories', CategoryViewSet, basename='category')
router.register('image_categories', ImageCategoryViewSet, basename='image_category')

urlpatterns = router.urls
