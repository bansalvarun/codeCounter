# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 12:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseTube.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('webpage', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('mapLocation', models.CharField(max_length=100)),
                ('startHour', models.IntegerField()),
                ('endHour', models.IntegerField()),
                ('establishedSince', models.IntegerField()),
                ('totalNumberStudents', models.IntegerField()),
                ('totalNumberFaculty', models.IntegerField()),
                ('facility', models.ManyToManyField(to='courseTube.Facility')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infrastructure', models.IntegerField()),
                ('qualityOfEducation', models.IntegerField()),
                ('workLoad', models.IntegerField()),
                ('feesWorth', models.IntegerField()),
                ('postCourseBenifits', models.IntegerField()),
                ('postCourseBenifitsText', models.CharField(blank=True, max_length=100, null=True)),
                ('recommendedFurther', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseTube.Institute')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('infrastructure', models.IntegerField()),
                ('qualityOfEducation', models.IntegerField()),
                ('workLoad', models.IntegerField()),
                ('feesWorth', models.IntegerField()),
                ('postCourseBenifits', models.IntegerField()),
                ('postCourseBenifitsText', models.CharField(blank=True, max_length=100, null=True)),
                ('recommendedFurther', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseTube.Institute')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.ManyToManyField(blank=True, null=True, to='courseTube.Institute')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WeekDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('note', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='reviewrequest',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseTube.Student'),
        ),
        migrations.AddField(
            model_name='review',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseTube.Student'),
        ),
        migrations.AddField(
            model_name='review',
            name='userDownVotes',
            field=models.ManyToManyField(blank=True, related_name='dislike', to='courseTube.Student'),
        ),
        migrations.AddField(
            model_name='review',
            name='userUpVotes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='courseTube.Student'),
        ),
        migrations.AddField(
            model_name='institute',
            name='tags',
            field=models.ManyToManyField(to='courseTube.Tag'),
        ),
        migrations.AddField(
            model_name='institute',
            name='weekdays',
            field=models.ManyToManyField(to='courseTube.WeekDays'),
        ),
        migrations.AddField(
            model_name='enroll',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseTube.Institute'),
        ),
        migrations.AddField(
            model_name='enroll',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseTube.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ManyToManyField(blank=True, null=True, to='courseTube.Faculty'),
        ),
        migrations.AddField(
            model_name='course',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courseTube.Institute'),
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(to='courseTube.Tag'),
        ),
    ]
