from celery import shared_task
from time import sleep


@shared_task
def sub(num1, num2):
    sleep(20)
    return num1-num2


# Task to practice celery beat or (celery periodic task)
@shared_task
def clear_cache(task_id):
    print(f"Session cache cleared: {task_id}")
    return task_id