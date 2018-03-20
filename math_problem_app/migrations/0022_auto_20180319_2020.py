# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-19 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0021_auto_20180318_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tests',
        ),
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.IntegerField(blank=True, choices=[(2, '칼럼'), (3, '커뮤니티'), (1, '소식')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='answerType',
            field=models.IntegerField(blank=True, choices=[(1, '객관식'), (2, '주관식')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.IntegerField(blank=True, choices=[(3, '어려움'), (1, '쉬움'), (2, '중간')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type1',
            field=models.IntegerField(blank=True, choices=[(1, '내신형'), (2, '수능형')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type2',
            field=models.IntegerField(blank=True, choices=[(1, '개념확인형'), (2, '개념응용형')], null=True),
        ),
        migrations.AlterField(
            model_name='problemunit',
            name='unit',
            field=models.IntegerField(blank=True, choices=[(3, '미적1'), (1, '수1'), (4, '미적2'), (5, '확통'), (2, '수2'), (6, '기벡')], null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, '일반'), (2, '진단고사')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.IntegerField(blank=True, choices=[(3, '3학년'), (2, '2학년'), (1, '1학년')], null=True),
        ),
    ]