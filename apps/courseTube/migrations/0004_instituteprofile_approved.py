# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseTube', '0003_instituteprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituteprofile',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
