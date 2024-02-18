from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Doctor, Appointment


# Create your views here.

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "service_app/doctors_list.html", context={"doctors": doctors})


def doctor_page(request, pk):
    doctor = Doctor.objects.get(id=pk)
    return render(request, 'service_app/doctor_page.html', context={"doctor": doctor})


def appointment_page(request, pk):
    doctor = Doctor.objects.get(id=pk)
    appointments = Appointment.objects.filter(doctor=doctor, enable=True)
    return render(request, "service_app/appointments_page.html", context={"appointments": appointments})


def appointment_book(doctor_pk, appointment_pk, patient_info):
    doctor = Doctor.objects.get(id=doctor_pk)
    appointment = Appointment.objects.get(doctor=doctor, id=appointment_pk)
    if appointment.enable is True:
        appointment.patient = patient_info
        appointment.booked = True
        appointment.save()

        return redirect("service_app:appointments", doctor_pk)
    else:
        return HttpResponse("Not enabled")


def patient_appointment(request, doctor_pk, appointment_pk):
    if request.method == "POST":
        patient_name = request.POST.get("patient_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        patient_info = f"{patient_name} - {phone_number} - {email}"

        return appointment_book(doctor_pk, appointment_pk, patient_info)
    else:
        return render(request, "service_app/appointment_book.html",
                      context={"doctor": doctor_pk, "appointment": appointment_pk})
