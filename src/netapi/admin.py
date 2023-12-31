from django.contrib import admin
from django.contrib.admin import register

from .models import *
# Register your models here.
@admin.register(ServerInfo)
class ServerInfoAdmin(admin.ModelAdmin):
    list_display = ['id','user','server_ip','plan_type'
        ,'created_at','expire_time','is_active']

admin.site.register(Plans)
admin.site.register(MonitorServer)