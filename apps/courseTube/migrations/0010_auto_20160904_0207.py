# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseTube', '0009_institute_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='institute',
            name='instituteUrl',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
