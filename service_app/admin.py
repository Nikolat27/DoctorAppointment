from django.contrib import admin
from . import models


# Register your models here.


class AppointmentAdmin(admin.TabularInline):
    model = models.Appointment


@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    inlines = [AppointmentAdmin]


admin.site.register(models.Proficiency)
admin.site.register(models.Klinik)
