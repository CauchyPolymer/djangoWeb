# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-17 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0017_auto_20180315_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('scoreSrl', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='rightAnswered',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='problem',
            name='totalAnswered',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='totalScore',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.IntegerField(blank=True, choices=[(3, '어려움'), (2, '중간'), (1, '쉬움')], null=True),
        ),
        migrations.AlterField(
            model_name='problemunit',
            name='unit',
            field=models.IntegerField(blank=True, choices=[(3, '미적1'), (2, '수2'), (6, '기벡'), (5, '확통'), (4, '미적2'), (1, '수1')], null=True),
        ),
        migrations.RemoveField(
            model_name='user',
            name='rate',
        ),
        migrations.AddField(
            model_name='user',
            name='rate',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.Rating'),
        ),
        migrations.AddField(
            model_name='test',
            name='scores',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.Score'),
        ),
    ]
