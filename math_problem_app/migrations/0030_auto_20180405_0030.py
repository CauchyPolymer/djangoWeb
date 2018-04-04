# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-05 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0029_auto_20180404_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isCardCertificate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.IntegerField(blank=True, choices=[(3, '커뮤니티'), (1, '소식'), (2, '칼럼')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='answerType',
            field=models.IntegerField(blank=True, choices=[(2, '주관식'), (1, '객관식')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.IntegerField(blank=True, choices=[(1, '쉬움'), (2, '중간'), (3, '어려움')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type2',
            field=models.IntegerField(blank=True, choices=[(1, '개념확인형'), (2, '개념응용형')], null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='type',
            field=models.IntegerField(blank=True, choices=[(2, '진단고사'), (3, '추천고사'), (1, '일반')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.IntegerField(blank=True, choices=[(2, '2학년'), (1, '1학년'), (3, '3학년')], null=True),
        ),
    ]