# Generated by Django 3.2.12 on 2022-04-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_alter_question_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
