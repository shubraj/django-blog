# Generated by Django 3.1.2 on 2020-11-16 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20201116_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilelog',
            name='ip_address',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='profilelog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_log', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profilelog',
            name='user_agent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
