# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseTube', '0008_institute_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
