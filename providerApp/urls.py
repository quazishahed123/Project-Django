from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from providerApp import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('', views.ClientList.as_view()),
    path('client/<int:pk>/', views.ClientDetail.as_view()),
    path('project/', views.ProjectList.as_view()),
    path('project/<int:pk>/', views.ProjectList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)