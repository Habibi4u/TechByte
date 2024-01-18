# Generated by Django 3.1.12 on 2023-03-11 09:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0014_auto_20230311_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='studentname',
            field=models.ForeignKey(
                default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
