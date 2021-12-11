from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from providerApp.serializer import UsermodelSerializer,ClientSerializer,ProjectSerializer
from providerApp.models import UserModel,ClientModel,ProjectModel
from rest_framework import generics


class UserList(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UsermodelSerializer


class ClientList(generics.ListCreateAPIView):
    queryset=ClientModel.objects.all()
    serializer_class=ClientSerializer



class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=ClientModel.objects.all()
    serializer_class=ClientSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset=ProjectModel.objects.all()
    serializer_class =ProjectSerializer



