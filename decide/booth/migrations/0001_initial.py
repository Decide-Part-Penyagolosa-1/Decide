# Generated by Django 2.0 on 2021-12-17 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotingCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.QuestionOption')),
                ('voting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.Voting')),
            ],
        ),
    ]
