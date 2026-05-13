
from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("details/", views.details, name="details"),
    path("student/", views.student, name="student"),
]