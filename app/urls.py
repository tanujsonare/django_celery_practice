from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("check_task_detail/<str:task_id>", views.check_task_detail, name="check_task_detail"),
]
