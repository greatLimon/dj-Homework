# Generated by Django 5.1.2 on 2024-10-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_alter_phone_image_alter_phone_name_alter_phone_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=256, unique=True),
        ),
    ]
