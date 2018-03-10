# Generated by Django 2.0.2 on 2018-03-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0011_auto_20180311_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.IntegerField(blank=True, choices=[(3, '진로'), (2, '칼럼'), (1, '소식')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.IntegerField(blank=True, choices=[(2, '중간'), (3, '어려움'), (1, '쉬움')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, '내신형'), (2, '수능형'), (4, '개념응용형'), (3, '개념확인형')], null=True),
        ),
        migrations.AlterField(
            model_name='problemunit',
            name='unit',
            field=models.IntegerField(blank=True, choices=[(5, '확통'), (3, '미적1'), (1, '수1'), (4, '미적2'), (2, '수2'), (6, '기벡')], null=True),
        ),
    ]
