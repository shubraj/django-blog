# Generated by Django 3.1.2 on 2020-11-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_profilelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilelog',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profilelog',
            name='country',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
