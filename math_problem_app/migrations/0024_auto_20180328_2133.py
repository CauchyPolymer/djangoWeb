# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-28 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0023_auto_20180326_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lectureSrl', models.AutoField(primary_key=True, serialize=False)),
                ('video', models.FileField(max_length=300, null=True, upload_to='videos/')),
                ('teacherName', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('recommendSrl', models.AutoField(primary_key=True, serialize=False)),
                ('aimGrade', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, '소식'), (2, '칼럼'), (3, '커뮤니티')], null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(max_length=300, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.IntegerField(blank=True, choices=[(2, '중간'), (1, '쉬움'), (3, '어려움')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type1',
            field=models.IntegerField(blank=True, choices=[(1, '내신형'), (2, '수능형')], null=True),
        ),
        migrations.AlterField(
            model_name='problemmiddleunit',
            name='middleUnit',
            field=models.IntegerField(blank=True, choices=[(2, '방정식과 부등식'), (17, '확률'), (13, '삼각함수'), (7, '지수와 로그'), (16, '순열과 조합'), (3, '도형의 방정식'), (1, '다항식'), (21, '공간도형과 공간좌표'), (18, '통계'), (14, '미분법'), (19, '이차곡선'), (20, '평면벡터'), (22, '공간벡터'), (8, '수열의 극한'), (10, '다항함수의 미분법'), (12, '지수함수와 로그함수'), (9, '함수의 극한'), (5, '함수'), (4, '집합과 명제'), (11, '다항함수의 적분법'), (15, '적분법'), (6, '수열')], null=True),
        ),
        migrations.AlterField(
            model_name='problemsmallunit',
            name='smallUnit',
            field=models.IntegerField(blank=True, choices=[(22, '상용로그'), (39, '여러가지 함수의 적분법'), (11, '도형의 이동'), (42, '순열과 조합'), (44, '확률의 뜻'), (50, '평면벡터의 뜻'), (9, '직선의 방정식'), (18, '무리식과 무리함수'), (23, '수열의 극한'), (47, '통계적 추정'), (28, '도함수의 활용'), (20, '여러가지 수열'), (25, '함수의 극한'), (19, '등차수열과 등비수열'), (8, '평면좌표'), (15, '절대부등식'), (48, '이차곡선의 방정식'), (40, '정적분의 활용'), (6, '여러가지 방정식'), (14, '명제'), (34, '삼각함수의 뜻'), (13, '집합'), (10, '원의 방정식'), (35, '삼각함수의 그래프'), (3, '인수분해'), (30, '정적분'), (38, '도함수의 활용'), (43, '이항정리'), (17, '유리식과 유리함수'), (31, '정적분의 활용'), (26, '함수의 연속'), (33, '지수함수와 로그함수의 미분'), (32, '지수함수와 로그함수의 뜻과 그래프'), (24, '급수'), (1, '다항식의 연산'), (49, '이차곡선과 접선의 방정식'), (36, '삼각함수의 미분'), (51, '평면운동'), (41, '경우의 수'), (7, '여러가지 부등식'), (2, '항등식과 나머지 정리'), (46, '확률변수와 확률분포'), (53, '공간좌표'), (29, '부정적분'), (52, '공간도형'), (45, '조건부 확률'), (4, '복소수와 이차방정식'), (21, '지수와 로그'), (12, '부등식의 영역'), (5, '이차방정식과 이차함수'), (37, '여러가지 함수의 미분법'), (27, '미분계수와 도함수'), (16, '함수'), (54, '공간벡터')], null=True),
        ),
        migrations.AlterField(
            model_name='problemunit',
            name='unit',
            field=models.IntegerField(blank=True, choices=[(4, '미적2'), (5, '확통'), (1, '수1'), (6, '기벡'), (2, '수2'), (3, '미적1')], null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, '일반'), (3, '추천고사'), (2, '진단고사')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.IntegerField(blank=True, choices=[(2, '2학년'), (1, '1학년'), (3, '3학년')], null=True),
        ),
        migrations.AddField(
            model_name='recommend',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='math_problem_app.ProblemUnit'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='unit',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.ProblemUnit'),
        ),
        migrations.AddField(
            model_name='user',
            name='recommend',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.Recommend'),
        ),
    ]
