# Generated by Django 3.0.7 on 2020-08-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0019_auto_20200826_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='posted_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
