# Generated by Django 3.0.7 on 2020-08-27 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0023_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.Blog'),
        ),
    ]
