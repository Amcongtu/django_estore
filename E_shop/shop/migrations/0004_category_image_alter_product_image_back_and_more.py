# Generated by Django 4.0.6 on 2022-10-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_status_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='shop/category/noImageCategory.png', upload_to='shop/category/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_back',
            field=models.ImageField(default='shop/noImageProduct.png', upload_to='shop/back/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_front',
            field=models.ImageField(default='shop/noImageProduct.png', upload_to='shop/front/'),
        ),
    ]