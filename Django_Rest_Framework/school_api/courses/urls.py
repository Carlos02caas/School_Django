from rest_framework import routers
from .views import CourseViewSet, CourseScheduleViewSet, AcademicPeriodViewSet

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'course-schedules', CourseScheduleViewSet)
router.register(r'academic-periods', AcademicPeriodViewSet)

urlpatterns = router.urls