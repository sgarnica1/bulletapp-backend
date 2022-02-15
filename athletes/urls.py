from cgitb import lookup
from email.mime import base
from django.urls import path, include
from .views import PlanView, ScheduleView, AthleteView, PaymentView, PlanAthletesView
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register('plans', PlanView)
plan_router = routers.NestedDefaultRouter(router, 'plans', lookup='plan')
plan_router.register('atletas', PlanAthletesView, basename='plan-atletas')

router.register('schedule', ScheduleView)
router.register('athletes', AthleteView)
router.register('payments', PaymentView)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(plan_router.urls))
]
