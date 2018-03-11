# Generated by Django 2.0.2 on 2018-03-12 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0014_merge_20180312_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.IntegerField(blank=True, choices=[(2, '칼럼'), (1, '소식'), (3, '진로')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='difficulty',
            field=models.IntegerField(blank=True, choices=[(3, '어려움'), (2, '중간'), (1, '쉬움')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type1',
            field=models.IntegerField(blank=True, choices=[(1, '내신형'), (2, '수능형')], null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type2',
            field=models.IntegerField(blank=True, choices=[(2, '개념응용형'), (1, '개념확인형')], null=True),
        ),
        migrations.AlterField(
            model_name='problemunit',
            name='unit',
            field=models.IntegerField(blank=True, choices=[(4, '미적2'), (3, '미적1'), (2, '수2'), (6, '기벡'), (1, '수1'), (5, '확통')], null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, '일반'), (2, '진단고사')], null=True),
        ),
    ]
