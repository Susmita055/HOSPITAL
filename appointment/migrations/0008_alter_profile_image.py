# Generated by Django 3.2.2 on 2021-06-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
