from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.images.views.image_viewsets import ImageViewSet
from apps.images.views.general_views import CategoryViewSet, ImageCategoryViewSet


router = SimpleRouter()
router.register('images', ImageViewSet, basename='images')
router.register('category', CategoryViewSet, basename='category')
router.register('image_category', ImageCategoryViewSet, basename='image_category')

urlpatterns = router.urls