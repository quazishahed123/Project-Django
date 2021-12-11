from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserModel,ClientModel,ProjectModel

class UsermodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClientModel
        fields= '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectModel
        fields= '__all__'
