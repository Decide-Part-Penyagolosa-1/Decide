# Generated by Django 4.0 on 2022-01-01 18:59

from django.db import migrations
from django.contrib.postgres.fields import JSONField


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='postproc',
            field=JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voting',
            name='tally',
            field=JSONField(blank=True, null=True),
        ),
    ]
