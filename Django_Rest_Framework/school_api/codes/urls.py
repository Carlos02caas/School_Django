from rest_framework import routers
from .views import PersonTypeViewSet, GenderViewSet, NationalityViewSet, MaritalStatusViewSet, StateViewSet

router = routers.DefaultRouter()
router.register(r'person-type', PersonTypeViewSet)
router.register(r'gender', GenderViewSet)
router.register(r'nationality', NationalityViewSet)
router.register(r'marital-status', MaritalStatusViewSet)
router.register(r'state', StateViewSet)

urlpatterns = router.urls