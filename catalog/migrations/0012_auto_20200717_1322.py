# Generated by Django 3.0.4 on 2020-07-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20200717_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realty',
            name='adaptation',
            field=models.CharField(max_length=255, verbose_name='Adaptation'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='area',
            field=models.CharField(max_length=255, verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='buiding',
            field=models.CharField(max_length=255, verbose_name='Buiding'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='floor_number',
            field=models.CharField(max_length=255, verbose_name='Floor number'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='namber_of_floors',
            field=models.CharField(max_length=255, verbose_name='Namber of floors'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='rooms',
            field=models.CharField(max_length=255, verbose_name='Rooms'),
        ),
    ]
