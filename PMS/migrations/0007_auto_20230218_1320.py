# Generated by Django 3.2.7 on 2023-02-18 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PMS', '0006_auto_20230218_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rows',
            name='total_rows',
        ),
        migrations.AddField(
            model_name='building',
            name='total_coloumn',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='building',
            name='total_rows',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.CreateModel(
            name='Coloumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coloumn_name', models.CharField(max_length=40)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS.building')),
                ('floor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS.floor')),
                ('rows_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS.rows')),
            ],
        ),
    ]
