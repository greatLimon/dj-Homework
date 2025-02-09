# Generated by Django 5.1.2 on 2024-10-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_phone_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.FloatField(max_length=128),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=256),
        ),
    ]
