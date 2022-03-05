from rest_framework.viewsets import ModelViewSet
from .serializers import PlanSerializer, ScheduleSerializer, AthleteSerializer, PaymentSerializer
from .models import Plan, Schedule, Athlete, Payment
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.shortcuts import redirect

import re


def redirect_view(request):
    response = redirect('/api')
    return response


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class PlanView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Plan.objects.all().order_by('id')
    serializer_class = PlanSerializer


class ScheduleView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Schedule.objects.all().order_by('hour')
    serializer_class = ScheduleSerializer


class AthleteView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Athlete.objects.all().order_by('-id')
    serializer_class = AthleteSerializer


class PaymentView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all().order_by('-id')

    def get_queryset(self):
        queryset = Payment.objects.all().order_by('-id')
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.all().filter(id=id)
        return queryset


class PlanAthletesView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AthleteSerializer

    def get_queryset(self):
        return Athlete.objects.filter(plan=self.kwargs['plan_pk'])
