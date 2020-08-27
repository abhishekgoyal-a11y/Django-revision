# Generated by Django 3.0.7 on 2020-08-24 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0013_auto_20200824_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
    ]