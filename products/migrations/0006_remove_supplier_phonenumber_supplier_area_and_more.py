# Generated by Django 4.0.3 on 2022-03-27 11:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='phoneNumber',
        ),
        migrations.AddField(
            model_name='supplier',
            name='area',
            field=models.CharField(choices=[('Bakery Products', 'Bakery Products'), ('Fresh Vegetables', 'Fresh Vegetables'), ('Fruits', 'Fuits'), ('Packaging', 'Packaging Material'), ('Pastry Products', 'Pastry Products'), ('Cleaning Products', 'Cleaning Products'), ('Services', 'Services'), ('Kitchen Products', 'Kitchen Products')], max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='mob_number',
            field=models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
        migrations.AddField(
            model_name='supplier',
            name='off_number',
            field=models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
