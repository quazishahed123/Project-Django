# Generated by Django 3.2 on 2021-12-10 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('providerApp', '0002_auto_20211210_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmodel',
            name='createdBy',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserModel', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ClientModel', to=settings.AUTH_USER_MODEL),
        ),
    ]
