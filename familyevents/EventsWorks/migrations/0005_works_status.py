# Generated by Django 5.0.2 on 2024-06-04 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventsWorks', '0004_works_booked_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
