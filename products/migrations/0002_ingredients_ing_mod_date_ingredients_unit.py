# Generated by Django 4.0.3 on 2022-03-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='ing_mod_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='unit',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
