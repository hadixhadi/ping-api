from django.http import JsonResponse
from rest_framework import serializers, status
from ..models import *
from ping3 import ping
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.shortcuts import redirect
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServerInfo
        fields='__all__'



class CreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        print("create serializer method")
        obj=ServerInfo.objects.create(**validated_data)
        return obj
    class Meta:
        model=ServerInfo
        read_only_fields=(
            'task',
            'expire_time',
            'is_active'
        )
        fields='__all__'

class RetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServerInfo
        fields='__all__'

class DeleteTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model=ServerInfo
        fields='__all__'

class MonitorServerSerializer(serializers.ModelSerializer):
    server=serializers.SerializerMethodField()
    server_user=serializers.SerializerMethodField()
    class Meta:
        model=MonitorServer
        fields=['response','server','server_user']

    def get_server(self,obj):
        return obj.server.server_ip
    def get_server_user(self,obj):
        return obj.server.user.email