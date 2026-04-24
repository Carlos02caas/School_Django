from rest_framework import routers
from .views import SchoolViewSet

router = routers.DefaultRouter()
router.register(r'school', SchoolViewSet)

urlpatterns = router.urls