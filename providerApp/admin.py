from django.contrib import admin
from providerApp.models import UserModel,ClientModel,ProjectModel

admin.site.register(UserModel)
admin.site.register(ClientModel)
admin.site.register(ProjectModel)