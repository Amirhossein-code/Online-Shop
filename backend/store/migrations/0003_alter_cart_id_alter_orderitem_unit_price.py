# Generated by Django 5.0.3 on 2024-03-19 08:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_productimage_image_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='unit_price',
            field=models.PositiveBigIntegerField(),
        ),
    ]
