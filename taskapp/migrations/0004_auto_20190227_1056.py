# Generated by Django 2.1.7 on 2019-02-27 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_auto_20190227_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='users',
            field=models.ManyToManyField(default=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_created', to=settings.AUTH_USER_MODEL, verbose_name='created by'), related_name='team_users', to=settings.AUTH_USER_MODEL, verbose_name='team_users'),
        ),
    ]
