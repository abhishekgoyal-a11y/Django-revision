# Generated by Django 3.0.7 on 2020-08-26 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0017_auto_20200824_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='message',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
