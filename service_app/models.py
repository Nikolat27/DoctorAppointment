from django.db import models
from django.utils import timezone
from persiantools.jdatetime import JalaliDate


# Create your models here.

class Proficiency(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='doctors_picture/')
    expertise = models.ForeignKey(Proficiency, on_delete=models.CASCADE, related_name='expertise')
    city = models.CharField(max_length=50)
    msn = models.IntegerField(unique=True)  # Medial services number
    description = models.TextField()
    phone_number = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.doctor_name


class Klinik(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='klinik')
    address = models.TextField()
    phone_number = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"Dr.{self.doctor.doctor_name} Klinik"


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField()
    enable = models.BooleanField(default=True, null=True, blank=True)
    booked = models.BooleanField(default=False, null=True, blank=True)
    patient = models.CharField(max_length=50, null=True, blank=True)

    # you can use patient with Foreign keys with user model too but i used char field for simplify

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.patient:
            self.booked = True
        else:
            self.booked = False

    def time_difference(self):
        now = timezone.now()
        difference = self.date - now
        day_difference = difference.days
        seconds_difference = difference.seconds
        hours_difference = seconds_difference // 3600
        minute_difference = (seconds_difference % 3600) // 60

        return f"Days difference: {day_difference} - Hours difference: {hours_difference} - Minute difference {minute_difference}"

    def JalaliDate(self):
        gregorian_date = self.date.date()
        jdate = JalaliDate(gregorian_date)
        persian_months = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar",
                          "Dey", "Bahman", "Esfand"]
        final_date = f"{jdate.day} / {persian_months[jdate.month - 1]} / {jdate.year}"
        return final_date

    def __str__(self):
        return self.doctor.doctor_name
