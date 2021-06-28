# Generated by Django 3.2.2 on 2021-06-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='mobile',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiology', 'Cardiology'), ('Dermatology', 'Dermatology'), ('Immunology', 'Immunology'), ('Anesthesiology', 'Anesthesiology'), ('Emergency', 'Emergency')], default='cardiologist', max_length=23),
        ),
    ]
