# Generated by Django 3.2.13 on 2022-10-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_product_image_products_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_img',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
