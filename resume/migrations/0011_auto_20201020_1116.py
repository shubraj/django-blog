# Generated by Django 3.1.2 on 2020-10-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_interest_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/'),
        ),
    ]
