# Generated by Django 3.0.4 on 2020-07-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20200704_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
