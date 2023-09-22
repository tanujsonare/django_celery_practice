from django.shortcuts import render
from celery.result import AsyncResult

from django_celery_practice.celery import add
# from .tasks import sub


# For practice using delay and apply_async function
# def home(request):
#     sum_result = add.delay(10, 5)
#     print("Sum result:", sum_result)
#     sub_result = sub.apply_async(args=[50, 10])
#     print("Substraction Result", sub_result)
#     return render(request, "app/home.html", {"sum_result": sum_result, "sub_result": sub_result})


def home(request):
    add_result = add.delay(30, 10)
    return render(request, "app/home.html", {"add_result": add_result})


def check_task_detail(request, task_id):
    task_detail = AsyncResult(task_id)
    print("Ready:", task_detail.ready())
    print("Successful:", task_detail.successful())
    print("Failed:", task_detail.failed())
    # print("Get:", task_detail.get()) # if we use this method then our functionality will work in synchronous form
    return render(request, "app/check_task_detail.html", {"task_detail": task_detail})

def contact(request):
    return render(request, "app/contact.html")


def about(request):
    return render(request, "app/about.html")
