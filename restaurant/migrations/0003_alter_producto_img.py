# Generated by Django 4.0.4 on 2022-05-11 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_producto_cod_prod_alter_producto_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.ImageField(upload_to='img/', verbose_name='Imagen'),
        ),
    ]
