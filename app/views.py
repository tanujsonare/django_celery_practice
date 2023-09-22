from django.shortcuts import render
from django_celery_practice.celery import add
# Create your views here.


def home(request):
    result = add.delay(10, 5)
    print("Result:", result)
    return render(request, "app/home.html", {"result": result})


def contact(request):
    return render(request, "app/contact.html")


def about(request):
    return render(request, "app/about.html")
