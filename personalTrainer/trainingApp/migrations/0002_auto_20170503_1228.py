# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='option_Stars',
            field=models.IntegerField(default=0, max_length=5),
        ),
    ]