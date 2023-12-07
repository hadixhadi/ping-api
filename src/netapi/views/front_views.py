import json
from django.shortcuts import render , HttpResponse , get_object_or_404
from rest_framework import viewsets
from netapi.models import *
from netapi.serializers.serilizers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from django.db import transaction
from rest_framework.exceptions import APIException
from django_celery_beat.models import IntervalSchedule, PeriodicTask
# Create your views here.
class ServerViewSet(viewsets.ModelViewSet):

    def get_permissions(self):
        permission_classes=[AllowAny]
        return [permission() for permission in permission_classes]
    def get_queryset(self):
        return ServerInfo.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        try:
            print("perform create method")
            # validate host name
            ping_status = ping(serializer.validated_data['server_ip'])
            if ping_status == False:
                raise ValidationError('this host name (ip) does not exist!')
            else:
                with transaction.atomic():
                    instance=serializer.save()
                    plan_type=instance.plan_type
                    schedule=IntervalSchedule.objects.create(
                            every=plan_type.plan_interval,
                            period=IntervalSchedule.MINUTES
                        )
                    task=PeriodicTask.objects.create(
                            name=f"monitor {instance.user}: {instance.server_ip}",
                            task="netapi.tasks.task_monitor",
                            interval=schedule,
                            kwargs=json.dumps({
                                "ServerInfoId":instance.id
                            }),
                            expires=timezone.now() + timedelta(days=5)
                        )
                    instance.task=task
                    instance.set_expire_time()
                    instance.is_active=True
                    instance.save()
                    return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            raise APIException(str(e))
    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        print(instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    def perform_destroy(self, instance):
        instance.delete()
    def get_serializer_class(self):
        match self.action:
            case "list":
               return ListSerializer
            case "create":
                return CreateSerializer
            case "retrieve":
                return RetrieveSerializer
            case "destroy":
                return DeleteTaskSerializer
            case _:
                return ListSerializer


class MonitorServerViewset(viewsets.ModelViewSet):
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    def get_queryset(self):
        return MonitorServer.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        match self.action:
            case "list":
                return MonitorServerSerializer
            case _:
                return MonitorServerSerializer