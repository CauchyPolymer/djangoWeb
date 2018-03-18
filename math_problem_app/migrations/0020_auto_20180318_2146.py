# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-18 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0019_auto_20180318_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.IntegerField(blank=True, choices=[(2, '칼럼'), (1, '소식'), (3, '커뮤니티')], null=True),
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
            field=models.IntegerField(blank=True, choices=[(6, '기벡'), (4, '미적2'), (2, '수2'), (1, '수1'), (5, '확통'), (3, '미적1')], null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, '일반'), (2, '진단고사')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
