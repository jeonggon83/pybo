# Generated by Django 4.2.7 on 2024-05-17 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0011_rename_author_answer_author_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='author_id',
            new_name='author',
        ),
    ]
