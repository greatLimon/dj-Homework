# Generated by Django 5.1.3 on 2024-11-09 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_tagsarticles_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagsarticles',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='articles.tags'),
        ),
    ]
