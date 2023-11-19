from netapi.utils.utils import *
from celery import shared_task
from celery import Celery
from config.celery.celery import app
from ping3 import ping
from config.envs.develop_settings import *
from django.utils import timezone
from .models import ServerInfo
@shared_task(bind=True)
def task_monitor(self,ServerInfoId):
    instance=ServerInfo.objects.get(pk=ServerInfoId)
    server_ip=instance.server_ip
    email=instance.email
    user=instance.user
    ping_status = ping(server_ip)
    if ping_status == None:
        message = f'Hi {user} server with tihs IP {server_ip} is not available'
        subject = "server lost!"
        send_email.delay(message=message, subject=subject, email_list=email)
    return "success"

@shared_task
def send_email(email_list,message,subject):
    subject = subject
    message = message
    email_from = develop_settings.EMAIL_HOST_USER
    recipient_list = [email_list,]
    mail_sent=send_mail(subject, message, email_from, recipient_list)
    return mail_sent




@shared_task(bind=True)
def run_is_active_function():
    ServerInfo.is_active()
