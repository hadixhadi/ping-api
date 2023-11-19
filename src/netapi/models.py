from django.db import models
from django.contrib.auth import get_user_model
from django_celery_beat.models import PeriodicTask
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
    def __str__(self):
        return f"{self.user}-{self.server_ip}-{self.email}"


class MonitorRequest(models.Model):
    response_time = models.IntegerField(blank=False)
    response_status = models.IntegerField(blank=False)
    monitor = models.ForeignKey(ServerInfo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
