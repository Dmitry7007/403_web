# Generated by Django 4.2.7 on 2023-12-01 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ManyToManyField(related_name='article_comments', to='main.comment'),
        ),
    ]
