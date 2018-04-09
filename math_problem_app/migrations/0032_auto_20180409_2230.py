# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-09 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0031_auto_20180407_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyDate',
            fields=[
                ('studyDateSrl', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='recommend',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recommend',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, '소식'), (2, '칼럼'), (3, '커뮤니티')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='answerType',
            field=models.IntegerField(blank=True, choices=[(2, '주관식'), (1, '객관식')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.IntegerField(blank=True, choices=[(3, '어려움'), (1, '쉬움'), (2, '중간')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type1',
            field=models.IntegerField(blank=True, choices=[(2, '수능형'), (1, '내신형')], null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, '일반'), (3, '추천고사'), (2, '진단고사')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.IntegerField(blank=True, choices=[(3, '3학년'), (2, '2학년'), (1, '1학년')], null=True),
        ),
        migrations.AddField(
            model_name='recommend',
            name='studyDate',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.StudyDate'),
        ),
    ]
