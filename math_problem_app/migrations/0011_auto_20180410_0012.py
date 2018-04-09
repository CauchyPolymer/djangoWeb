# Generated by Django 2.0.2 on 2018-04-10 00:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0010_auto_20180408_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyDate',
            fields=[
                ('studyDateSrl', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('smallUnit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='math_problem_app.ProblemSmallUnit')),
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
            field=models.IntegerField(blank=True, choices=[(3, '커뮤니티'), (1, '소식'), (2, '칼럼')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='answerType',
            field=models.IntegerField(blank=True, choices=[(1, '객관식'), (2, '주관식')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.IntegerField(blank=True, choices=[(2, '중간'), (1, '쉬움'), (3, '어려움')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type2',
            field=models.IntegerField(blank=True, choices=[(2, '개념응용형'), (1, '개념확인형')], null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, '일반'), (3, '추천고사'), (2, '진단고사')], null=True),
        ),
        migrations.AddField(
            model_name='recommend',
            name='studyDate',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.StudyDate'),
        ),
    ]
