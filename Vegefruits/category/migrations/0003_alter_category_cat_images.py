# Generated by Django 4.2 on 2023-05-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_cat_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_images',
            field=models.ImageField(upload_to='images'),
        ),
    ]