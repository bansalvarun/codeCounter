# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseTube', '0016_auto_20160904_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='logo',
            field=models.CharField(default='https://placeholdit.imgix.net/~text?txtsize=33&txt=350%C3%97150&w=350&h=150', max_length=100),
        ),
    ]
