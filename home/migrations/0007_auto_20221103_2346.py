# Generated by Django 3.2.13 on 2022-11-03 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_order_items_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='pin',
            field=models.CharField(max_length=10),
        ),
    ]
