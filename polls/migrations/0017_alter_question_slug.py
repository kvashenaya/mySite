# Generated by Django 3.2.12 on 2022-03-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(default=6, max_length=25),
        ),
    ]