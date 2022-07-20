from rest_framework.routers import SimpleRouter

from .views import UserViewSet


__author__ = "Ricardo"
__version__ = "0.1"


router = SimpleRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = router.urls
