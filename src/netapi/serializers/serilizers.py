from django.http import JsonResponse
from rest_framework import serializers, status
from ..models import *
from ..utils.utils import send_ping
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
