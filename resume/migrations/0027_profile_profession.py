# Generated by Django 3.1.2 on 2020-10-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0026_auto_20201024_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
