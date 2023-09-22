from celery import shared_task
from time import sleep


@shared_task
def sub(num1, num2):
    sleep(20)
    return num1-num2