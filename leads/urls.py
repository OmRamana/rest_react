from rest_framework import routers
from .api import leadViewSet, viewsets


router = routers.DefaultRouter
router.register('api/leads',leadViewSet,'leads')

urlpatterns = router.urls