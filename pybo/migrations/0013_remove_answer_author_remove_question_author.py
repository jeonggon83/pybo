# Generated by Django 4.2.7 on 2024-05-17 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0012_rename_author_id_answer_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
    ]
