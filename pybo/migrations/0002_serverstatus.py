# Generated by Django 4.0.3 on 2024-05-02 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerStatus',
            fields=[
                ('no', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='NO')),
                ('temperature', models.TextField()),
            ],
        ),
    ]
