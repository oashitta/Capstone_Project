# Generated by Django 4.1.3 on 2022-11-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_rename_is_right_answer_is_correct_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='technique',
            field=models.IntegerField(choices=[(0, 'Multiple Choice'), (1, 'Fill in the Gap'), (2, 'Short Answer'), (3, 'True or False')], default=0, verbose_name='Question Type'),
        ),
    ]
