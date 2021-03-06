# Generated by Django 3.0.4 on 2020-07-17 13:17

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20200704_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realty',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='realty',
            name='long',
        ),
        migrations.AddField(
            model_name='realty',
            name='address',
            field=django_google_maps.fields.AddressField(default='Любляна', max_length=200),
        ),
        migrations.AddField(
            model_name='realty',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(default='46.05187370933915,14.506043267333983', max_length=100),
        ),
    ]
