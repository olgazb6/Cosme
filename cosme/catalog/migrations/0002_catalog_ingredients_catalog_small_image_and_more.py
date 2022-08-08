# Generated by Django 4.0.6 on 2022-07-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='ingredients',
            field=models.TextField(default='-'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalog',
            name='small_image',
            field=models.ImageField(default='-', upload_to='catalog/static/catalog/img/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='catalog',
            name='image',
            field=models.ImageField(upload_to='catalog/static/catalog/img/'),
        ),
    ]