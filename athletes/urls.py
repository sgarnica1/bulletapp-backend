from django.urls import path, include
from .views import PlanView, ScheduleView, AthleteView, PaymentView, PlanAthletesView, MyTokenObtainPairView
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = routers.DefaultRouter()

router.register('plans', PlanView)
plan_router = routers.NestedDefaultRouter(router, 'plans', lookup='plan')
plan_router.register('atletas', PlanAthletesView, basename='plan-atletas')

router.register('schedule', ScheduleView)
router.register('athletes', AthleteView)
router.register('payments', PaymentView)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(plan_router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
