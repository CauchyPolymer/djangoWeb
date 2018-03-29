# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-28 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0025_auto_20180328_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='middleUnit',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.ProblemMiddleUnit'),
        ),
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.IntegerField(blank=True, choices=[(2, '칼럼'), (1, '소식'), (3, '커뮤니티')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='answerType',
            field=models.IntegerField(blank=True, choices=[(2, '주관식'), (1, '객관식')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.IntegerField(blank=True, choices=[(3, '어려움'), (2, '중간'), (1, '쉬움')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type1',
            field=models.IntegerField(blank=True, choices=[(2, '수능형'), (1, '내신형')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type2',
            field=models.IntegerField(blank=True, choices=[(2, '개념응용형'), (1, '개념확인형')], null=True),
        ),
        migrations.AlterField(
            model_name='problemmiddleunit',
            name='middleUnit',
            field=models.IntegerField(blank=True, choices=[(1, '다항식'), (2, '방정식과 부등식'), (3, '도형의 방정식'), (4, '집합과 명제'), (5, '함수'), (6, '수열'), (7, '지수와 로그'), (8, '수열의 극한'), (9, '함수의 극한'), (10, '다항함수의 미분법'), (11, '다항함수의 적분법'), (12, '지수함수와 로그함수'), (13, '삼각함수'), (14, '미분법'), (15, '적분법'), (16, '순열과 조합'), (17, '확률'), (18, '통계'), (19, '이차곡선'), (20, '평면벡터'), (21, '공간도형과 공간좌표'), (22, '공간벡터')], null=True),
        ),
        migrations.AlterField(
            model_name='problemsmallunit',
            name='smallUnit',
            field=models.IntegerField(blank=True, choices=[(1, '다항식의 연산'), (2, '항등식과 나머지 정리'), (3, '인수분해'), (4, '복소수와 이차방정식'), (5, '이차방정식과 이차함수'), (6, '여러가지 방정식'), (7, '여러가지 부등식'), (8, '평면좌표'), (9, '직선의 방정식'), (10, '원의 방정식'), (11, '도형의 이동'), (12, '부등식의 영역'), (13, '집합'), (14, '명제'), (15, '절대부등식'), (16, '함수'), (17, '유리식과 유리함수'), (18, '무리식과 무리함수'), (19, '등차수열과 등비수열'), (20, '여러가지 수열'), (21, '지수와 로그'), (22, '상용로그'), (23, '수열의 극한'), (24, '급수'), (25, '함수의 극한'), (26, '함수의 연속'), (27, '미분계수와 도함수'), (28, '도함수의 활용'), (29, '부정적분'), (30, '정적분'), (31, '정적분의 활용'), (32, '지수함수와 로그함수의 뜻과 그래프'), (33, '지수함수와 로그함수의 미분'), (34, '삼각함수의 뜻'), (35, '삼각함수의 그래프'), (36, '삼각함수의 미분'), (37, '여러가지 함수의 미분법'), (38, '도함수의 활용'), (39, '여러가지 함수의 적분법'), (40, '정적분의 활용'), (41, '경우의 수'), (42, '순열과 조합'), (43, '이항정리'), (44, '확률의 뜻'), (45, '조건부 확률'), (46, '확률변수와 확률분포'), (47, '통계적 추정'), (48, '이차곡선의 방정식'), (49, '이차곡선과 접선의 방정식'), (50, '평면벡터의 뜻'), (51, '평면운동'), (52, '공간도형'), (53, '공간좌표'), (54, '공간벡터')], null=True),
        ),
        migrations.AlterField(
            model_name='problemunit',
            name='unit',
            field=models.IntegerField(blank=True, choices=[(1, '수1'), (2, '수2'), (3, '미적1'), (4, '미적2'), (5, '확통'), (6, '기벡')], null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='type',
            field=models.IntegerField(blank=True, choices=[(2, '진단고사'), (3, '추천고사'), (1, '일반')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.IntegerField(blank=True, choices=[(1, '1학년'), (2, '2학년'), (3, '3학년')], null=True),
        ),
    ]
