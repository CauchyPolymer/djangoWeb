# Generated by Django 2.0.2 on 2018-03-29 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answerSrl', models.AutoField(primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerNum',
            fields=[
                ('answerNumSrl', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('boardSrl', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('text', models.TextField(blank=True, max_length=10000, null=True)),
                ('viewCnt', models.IntegerField(blank=True, default=0, null=True)),
                ('recommendCnt', models.IntegerField(blank=True, default=0, null=True)),
                ('type', models.IntegerField(blank=True, choices=[(1, '소식'), (3, '커뮤니티'), (2, '칼럼')], null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentSrl', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(blank=True, max_length=5000, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lectureSrl', models.AutoField(primary_key=True, serialize=False)),
                ('video', models.FileField(max_length=300, null=True, upload_to='videos/')),
                ('teacherName', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photoSrl', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(max_length=300, null=True, upload_to='photos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('problemSrl', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(blank=True, max_length=2000, null=True)),
                ('answer', models.IntegerField(blank=True, null=True)),
                ('type1', models.IntegerField(blank=True, choices=[(1, '내신형'), (2, '수능형')], null=True)),
                ('type2', models.IntegerField(blank=True, choices=[(1, '개념확인형'), (2, '개념응용형')], null=True)),
                ('difficulty', models.IntegerField(blank=True, choices=[(1, '쉬움'), (2, '중간'), (3, '어려움')], null=True)),
                ('answerType', models.IntegerField(blank=True, choices=[(2, '주관식'), (1, '객관식')], default=1, null=True)),
                ('explanation', models.TextField(blank=True, max_length=10000, null=True)),
                ('totalAnswered', models.IntegerField(default=0)),
                ('rightAnswered', models.IntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemMiddleUnit',
            fields=[
                ('problemMiddleUnitSrl', models.AutoField(primary_key=True, serialize=False)),
                ('middleUnit', models.IntegerField(blank=True, choices=[(1, '다항식'), (2, '방정식과 부등식'), (3, '도형의 방정식'), (4, '집합과 명제'), (5, '함수'), (6, '수열'), (7, '지수와 로그'), (8, '수열의 극한'), (9, '함수의 극한'), (10, '다항함수의 미분법'), (11, '다항함수의 적분법'), (12, '지수함수와 로그함수'), (13, '삼각함수'), (14, '미분법'), (15, '적분법'), (16, '순열과 조합'), (17, '확률'), (18, '통계'), (19, '이차곡선'), (20, '평면벡터'), (21, '공간도형과 공간좌표'), (22, '공간벡터')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemSmallUnit',
            fields=[
                ('problemSmallUnitSrl', models.AutoField(primary_key=True, serialize=False)),
                ('smallUnit', models.IntegerField(blank=True, choices=[(1, '다항식의 연산'), (2, '항등식과 나머지 정리'), (3, '인수분해'), (4, '복소수와 이차방정식'), (5, '이차방정식과 이차함수'), (6, '여러가지 방정식'), (7, '여러가지 부등식'), (8, '평면좌표'), (9, '직선의 방정식'), (10, '원의 방정식'), (11, '도형의 이동'), (12, '부등식의 영역'), (13, '집합'), (14, '명제'), (15, '절대부등식'), (16, '함수'), (17, '유리식과 유리함수'), (18, '무리식과 무리함수'), (19, '등차수열과 등비수열'), (20, '여러가지 수열'), (21, '지수와 로그'), (22, '상용로그'), (23, '수열의 극한'), (24, '급수'), (25, '함수의 극한'), (26, '함수의 연속'), (27, '미분계수와 도함수'), (28, '도함수의 활용'), (29, '부정적분'), (30, '정적분'), (31, '정적분의 활용'), (32, '지수함수와 로그함수의 뜻과 그래프'), (33, '지수함수와 로그함수의 미분'), (34, '삼각함수의 뜻'), (35, '삼각함수의 그래프'), (36, '삼각함수의 미분'), (37, '여러가지 함수의 미분법'), (38, '도함수의 활용'), (39, '여러가지 함수의 적분법'), (40, '정적분의 활용'), (41, '경우의 수'), (42, '순열과 조합'), (43, '이항정리'), (44, '확률의 뜻'), (45, '조건부 확률'), (46, '확률변수와 확률분포'), (47, '통계적 추정'), (48, '이차곡선의 방정식'), (49, '이차곡선과 접선의 방정식'), (50, '평면벡터의 뜻'), (51, '평면운동'), (52, '공간도형'), (53, '공간좌표'), (54, '공간벡터')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemUnit',
            fields=[
                ('problemUnitSrl', models.AutoField(primary_key=True, serialize=False)),
                ('unit', models.IntegerField(blank=True, choices=[(1, '수1'), (2, '수2'), (3, '미적1'), (4, '미적2'), (5, '확통'), (6, '기벡')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('ratingSrl', models.AutoField(primary_key=True, serialize=False)),
                ('su1', models.IntegerField(blank=True, null=True)),
                ('su2', models.IntegerField(blank=True, null=True)),
                ('mi1', models.IntegerField(blank=True, null=True)),
                ('mi2', models.IntegerField(blank=True, null=True)),
                ('givec', models.IntegerField(blank=True, null=True)),
                ('hwaktong', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(default=0)),
                ('totalScore', models.IntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('recommendSrl', models.AutoField(primary_key=True, serialize=False)),
                ('aimGrade', models.IntegerField(blank=True, null=True)),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='math_problem_app.ProblemUnit')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('scoreSrl', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('testSrl', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.IntegerField(blank=True, choices=[(3, '추천고사'), (2, '진단고사'), (1, '일반')], null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('problems', models.ManyToManyField(blank=True, null=True, to='math_problem_app.Problem')),
                ('scores', models.ManyToManyField(blank=True, null=True, to='math_problem_app.Score')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userSrl', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(blank=True, max_length=200, null=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('sex', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('school', models.CharField(blank=True, max_length=200, null=True)),
                ('grade', models.IntegerField(blank=True, choices=[(1, '1학년'), (3, '3학년'), (2, '2학년')], null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('answers', models.ManyToManyField(blank=True, null=True, to='math_problem_app.Answer')),
                ('recommend', models.ManyToManyField(blank=True, null=True, to='math_problem_app.Recommend')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='math_problem_app.User'),
        ),
        migrations.AddField(
            model_name='problem',
            name='middleUnit',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.ProblemMiddleUnit'),
        ),
        migrations.AddField(
            model_name='problem',
            name='photos',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.Photo'),
        ),
        migrations.AddField(
            model_name='problem',
            name='smallUnit',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.ProblemSmallUnit'),
        ),
        migrations.AddField(
            model_name='problem',
            name='unit',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.ProblemUnit'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='middleUnit',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.ProblemMiddleUnit'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='unit',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.ProblemUnit'),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='math_problem_app.User'),
        ),
        migrations.AddField(
            model_name='board',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.Comment'),
        ),
        migrations.AddField(
            model_name='board',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='math_problem_app.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answers',
            field=models.ManyToManyField(blank=True, null=True, related_name='answers', to='math_problem_app.AnswerNum'),
        ),
        migrations.AddField(
            model_name='answer',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_problem_app.Test'),
        ),
    ]
