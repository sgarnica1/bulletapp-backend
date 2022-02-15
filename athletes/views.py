from rest_framework.viewsets import ModelViewSet
from .serializers import PlanSerializer, ScheduleSerializer, AthleteSerializer, PaymentSerializer
from .models import Plan, Schedule, Athlete, Payment


class PlanView(ModelViewSet):
    queryset = Plan.objects.all().order_by('id')
    serializer_class = PlanSerializer


class ScheduleView(ModelViewSet):
    queryset = Schedule.objects.all().order_by('-id')
    serializer_class = ScheduleSerializer


class AthleteView(ModelViewSet):
    queryset = Athlete.objects.all().order_by('-id')
    serializer_class = AthleteSerializer


class PaymentView(ModelViewSet):
    queryset = Payment.objects.all().order_by('-id')
    serializer_class = PaymentSerializer


class PlanAthletesView(ModelViewSet):
    serializer_class = AthleteSerializer

    def get_queryset(self):
        return Athlete.objects.filter(plan=self.kwargs['plan_pk'])
