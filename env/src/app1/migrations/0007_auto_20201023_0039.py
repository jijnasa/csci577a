# Generated by Django 3.1.2 on 2020-10-23 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20201023_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='caregiver',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/person_avatar.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 23, 0, 39, 14, 915691)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 23, 0, 39, 14, 915691)),
        ),
        migrations.AlterField(
            model_name='senior',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/person_avatar.png', upload_to='images/'),
        ),
    ]
