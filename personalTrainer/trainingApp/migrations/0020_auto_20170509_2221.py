# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingApp', '0019_auto_20170509_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutschedule',
            name='date_WO',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='workoutschedule',
            name='time_of_day',
            field=models.TimeField(blank=True),
        ),
    ]
