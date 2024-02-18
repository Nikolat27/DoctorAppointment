from . import views
from django.urls import path

app_name = "service_app"
urlpatterns = [
    path("appointments/<int:pk>", views.appointment_page, name="appointments"),
    path("doctors_list", views.doctor_list, name="doctors_list"),
    path("doctor_detail/<int:pk>", views.doctor_page, name="doctor_detail"),
    path("patient_register/<int:doctor_pk>/<int:appointment_pk>", views.patient_appointment, name="patient_register"),
]