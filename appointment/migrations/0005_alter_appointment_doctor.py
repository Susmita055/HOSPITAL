# Generated by Django 3.2.2 on 2021-06-24 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_auto_20210620_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor'),
        ),
    ]