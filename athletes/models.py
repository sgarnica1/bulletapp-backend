from django.db import models

# Create your models here.


class Plan(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Schedule(models.Model):
    hour = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return str(self.hour)


class Athlete(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL,
                             null=True, blank=False, related_name='plan')
    beneficiary = models.OneToOneField(
        'self', on_delete=models.SET_NULL, null=True, blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL,
                                 null=True, blank=False, related_name='athlete_schedule')
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} - {self.schedule} / {self.plan}'


class Payment(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE,
                                null=False, blank=False, related_name="athlete_payment")
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL,
                             null=True, blank=False, related_name="athlete_plan")
    quantity = models.DecimalField(decimal_places=2, max_digits=10)
    beneficiary = models.ForeignKey(Athlete, on_delete=models.SET_NULL,
                                    null=True, blank=True, related_name="payment_benficiary")
    date = models.DateTimeField(auto_now=True)
