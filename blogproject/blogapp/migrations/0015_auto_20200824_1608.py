# Generated by Django 3.0.7 on 2020-08-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_auto_20200824_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='images/default.jpg', null=True, upload_to='images/'),
        ),
    ]
