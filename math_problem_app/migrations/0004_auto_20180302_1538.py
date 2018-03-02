# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-02 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('math_problem_app', '0003_auto_20180302_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answerSrl', models.AutoField(primary_key=True, serialize=False)),
                ('a1', models.IntegerField(blank=True, null=True)),
                ('a2', models.IntegerField(blank=True, null=True)),
                ('a3', models.IntegerField(blank=True, null=True)),
                ('a4', models.IntegerField(blank=True, null=True)),
                ('a5', models.IntegerField(blank=True, null=True)),
                ('a6', models.IntegerField(blank=True, null=True)),
                ('a7', models.IntegerField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photoSrl', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(max_length=200, null=True, upload_to='resource/photos/0e9f5c6e-ed59-4efe-a172-f6918c830225')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('problemSrl', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(blank=True, max_length=2000, null=True)),
                ('answer', models.IntegerField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('photo1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo1', to='math_problem_app.Photo')),
                ('photo2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo2', to='math_problem_app.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('testSrl', models.AutoField(primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('p1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p1', to='math_problem_app.Problem')),
                ('p2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p2', to='math_problem_app.Problem')),
                ('p3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p3', to='math_problem_app.Problem')),
                ('p4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p4', to='math_problem_app.Problem')),
                ('p5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p5', to='math_problem_app.Problem')),
                ('p6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p6', to='math_problem_app.Problem')),
                ('p7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p7', to='math_problem_app.Problem')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_problem_app.Test'),
        ),
        migrations.AddField(
            model_name='user',
            name='answers',
            field=models.ManyToManyField(blank=True, null=True, to='math_problem_app.Answer'),
        ),
    ]
