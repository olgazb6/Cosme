# Generated by Django 4.0.6 on 2022-08-01 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_catalog_ingredients_catalog_small_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='small_image',
        ),
    ]
