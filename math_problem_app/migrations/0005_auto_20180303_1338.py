# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-03 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0004_auto_20180302_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(max_length=200, null=True, upload_to='resource/photos/adaf4207-6b16-4644-8c16-98870f23cc25'),
        ),
    ]