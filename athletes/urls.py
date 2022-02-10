from django.urls import path, include
from .views import PlanView, ScheduleView, AthleteView, PaymentView
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('plans', PlanView)
router.register('schedule', ScheduleView)
router.register('athletes', AthleteView)
router.register('payments', PaymentView)

urlpatterns = [
    path('', include(router.urls))
]
