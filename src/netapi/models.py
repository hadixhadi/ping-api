import datetime
from django.utils import timezone
from datetime import timedelta
from django.db import models
from django.contrib.auth import get_user_model
from django_celery_beat.models import PeriodicTask
import time
# Create your models here.

class Plans(models.Model):
    plan_name=models.CharField(max_length=200,null=True,blank=True) #change null and blank after test
    plan_interval=models.IntegerField()
    plan_description=models.TextField(max_length=300)

    def __str__(self):
        return f"every {self.plan_interval} min"
    class Meta:
        verbose_name='Plan'




class ServerInfo(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    email=models.EmailField(max_length=300,null=True,blank=True)
    server_ip=models.TextField(max_length=100,null=True,blank=True)
    plan_type=models.ForeignKey(Plans,null=True,on_delete=models.SET_NULL)
    task=models.ForeignKey(PeriodicTask,null=True,blank=True,on_delete=models.SET_NULL)
    created_at=models.DateTimeField(auto_now_add=True)
    expire_time=models.DateTimeField(blank=True,null=True)
    is_active=models.BooleanField(default=False,null=True)
    def set_expire_time(self):
        self.expire_time=timezone.now() + timedelta(days=30)
        self.save()
    @classmethod
    def is_expired(self):
        if self.expire_time < timezone.now():
            self.is_active=False
    def __str__(self):
        return f"{self.user}-{self.server_ip}-{self.email}"


