# Generated by Django 3.0.7 on 2020-08-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='message',
            field=models.TextField(max_length=100, null=True),
        ),
    ]