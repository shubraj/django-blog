# Generated by Django 3.1.2 on 2020-10-23 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0020_auto_20201023_0337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workflow',
            name='completed',
        ),
    ]
