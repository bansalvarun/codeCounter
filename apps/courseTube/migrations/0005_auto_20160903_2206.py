# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseTube', '0004_instituteprofile_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='registeredBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courseTube.InstituteProfile'),
        ),
    ]