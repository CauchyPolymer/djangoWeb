# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-11 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0011_auto_20180311_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tests',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.Test'),
        ),
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.IntegerField(blank=True, choices=[(3, '진로'), (2, '칼럼'), (1, '소식')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.IntegerField(blank=True, choices=[(1, '쉬움'), (2, '중간'), (3, '어려움')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type1',
            field=models.IntegerField(blank=True, choices=[(2, '수능형'), (1, '내신형')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type2',
            field=models.IntegerField(blank=True, choices=[(1, '개념확인형'), (2, '개념응용형')], null=True),
        ),
        migrations.AlterField(
            model_name='problemunit',
            name='unit',
            field=models.IntegerField(blank=True, choices=[(4, '미적2'), (2, '수2'), (3, '미적1'), (6, '기벡'), (1, '수1'), (5, '확통')], null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='type',
            field=models.IntegerField(blank=True, choices=[(2, '진단고사'), (1, '일반')], null=True),
        ),
    ]
