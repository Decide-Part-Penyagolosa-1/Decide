# Generated by Django 2.0 on 2021-12-20 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_auto_20211220_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='yes_no_question',
        ),
        migrations.AddField(
            model_name='question',
            name='binary_question',
            field=models.BooleanField(default=False, help_text='Check the box to generate a binary question', verbose_name='Answers Yes/No'),
        ),
    ]
