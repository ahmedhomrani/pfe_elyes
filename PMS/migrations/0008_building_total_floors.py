# Generated by Django 3.2.7 on 2023-02-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMS', '0007_auto_20230218_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='total_floors',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
