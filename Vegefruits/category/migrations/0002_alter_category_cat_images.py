# Generated by Django 4.2 on 2023-05-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_images',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]
