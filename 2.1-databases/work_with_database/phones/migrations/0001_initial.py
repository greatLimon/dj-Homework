# Generated by Django 5.1.2 on 2024-10-26 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=20)),
                ('image', models.BinaryField()),
                ('release_data', models.DateField()),
                ('lte_exist', models.BooleanField()),
                ('slug', models.SlugField(max_length=20)),
            ],
        ),
    ]
