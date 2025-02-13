# Generated by Django 5.1.6 on 2025-02-13 18:34

import productos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_imagen_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, default='productos/no_image.png', null=True, upload_to=productos.models.product_image_path),
        ),
    ]
