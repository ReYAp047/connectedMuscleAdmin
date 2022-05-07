# Generated by Django 3.2 on 2022-05-07 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_recommended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='Category',
            field=models.ManyToManyField(default=None, to='product.ProductCategory'),
        ),
    ]
