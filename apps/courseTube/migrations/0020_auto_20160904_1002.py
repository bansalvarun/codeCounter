# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseTube', '0019_auto_20160904_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(related_name='courses', to='courseTube.Tag'),
        ),
    ]
