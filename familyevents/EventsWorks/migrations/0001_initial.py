# Generated by Django 5.0.2 on 2024-04-26 17:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('place', models.CharField(max_length=500)),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_type', to='services.services')),
            ],
        ),
        migrations.CreateModel(
            name='BookedWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booked_workers', to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booked_works', to='EventsWorks.works')),
            ],
        ),
    ]
