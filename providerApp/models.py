from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class UserModel(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=20)
    empid = models.CharField(max_length=10)

    def __str__(self):
        return "{} - {}".format(self.name, self.empid)


class ClientModel(models.Model):
    projectName = models.CharField(max_length=20)
    companyName = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey('UserModel',related_name='usename',on_delete=CASCADE)

    def __str__(self):
        return "{} - {}".format(self.projectName, self.companyName)

class ProjectModel(models.Model):
    projectName = models.CharField(max_length=30)
    clientName = models.OneToOneField(ClientModel,on_delete=CASCADE)
    user = models.OneToOneField('auth.User',related_name='ClientModel',on_delete=CASCADE)

    def __str__(self):
        return "{} - {}".format(self.projectName, self.user)