# Generated by Django 3.2 on 2021-09-15 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variants',
            name='product_variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.products'),
        ),
    ]
