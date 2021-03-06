# Generated by Django 3.0.4 on 2020-07-03 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_user', models.CharField(choices=[('seller', 'Seller'), ('buyer', 'Buyer')], default='seller', max_length=100, verbose_name='Type User')),
                ('telephone', models.BigIntegerField(blank=True, null=True, verbose_name='Phone')),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'user data',
                'verbose_name_plural': 'user data',
            },
        ),
    ]
