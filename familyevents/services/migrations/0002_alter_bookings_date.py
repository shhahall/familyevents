# Generated by Django 5.0.2 on 2024-05-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
