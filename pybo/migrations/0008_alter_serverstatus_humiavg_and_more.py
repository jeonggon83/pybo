# Generated by Django 4.0.3 on 2024-05-07 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_alter_serverstatus_reg_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverstatus',
            name='humiAVG',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='serverstatus',
            name='tempAVG',
            field=models.CharField(max_length=5),
        ),
    ]
