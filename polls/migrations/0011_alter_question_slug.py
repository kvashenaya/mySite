# Generated by Django 3.2.12 on 2022-03-23 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(max_length=25, unique=True),
        ),
    ]
