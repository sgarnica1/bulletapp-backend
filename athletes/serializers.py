from .models import Plan, Schedule, Athlete, Payment
from rest_framework import serializers


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'price']


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'hour']


class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = ['id', 'first_name', 'last_name',
                  'email', 'phone_number', 'plan', 'schedule', 'beneficiary', 'created']


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'athlete', 'plan', 'quantity', 'beneficiary', 'date']
