# Generated by Django 3.2.12 on 2022-03-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_max'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='min',
            field=models.IntegerField(default=10000),
        ),
    ]