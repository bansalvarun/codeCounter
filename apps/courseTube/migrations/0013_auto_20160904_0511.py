# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseTube', '0012_auto_20160904_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='feesWorth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='infrastructure',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='postCourseBenifits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='qualityOfEducation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='workLoad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]