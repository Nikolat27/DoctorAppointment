from . import views
from django.urls import path

app_name = "home_app"
urlpatterns = [
    path('', views.home_page, name="main"),
    path('about-contact', views.about_page, name="about-contact"),
]
