from celery import shared_task
from django.core.mail import send_mail

@shared_task(bind=True)
def CustomTask(self):
    for i in range(0,10):
        print(i)
    return "Done"