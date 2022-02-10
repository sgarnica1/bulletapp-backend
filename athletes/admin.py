from django.contrib import admin
from .models import Plan, Schedule, Athlete, Payment

# Register your models here.


class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', ]


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['hour', ]


class AthleteAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'plan', 'schedule']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['athlete', 'plan', 'quantity', ]


admin.site.register(Plan, PlanAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Athlete, AthleteAdmin)
admin.site.register(Payment, PaymentAdmin)
