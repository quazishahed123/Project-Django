# Generated by Django 3.2 on 2021-12-11 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providerApp', '0004_auto_20211211_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientmodel',
            name='createdBy',
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='createdBy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usename', to='providerApp.usermodel'),
            preserve_default=False,
        ),
    ]
