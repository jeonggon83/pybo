# Generated by Django 4.2.7 on 2024-05-17 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0010_answer_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='author',
            new_name='author_id',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='author',
            new_name='author_id',
        ),
    ]
