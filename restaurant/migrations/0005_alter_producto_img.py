# Generated by Django 4.0.4 on 2022-05-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_producto_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.ImageField(upload_to='img/', verbose_name='Imagen'),
        ),
    ]