# Generated by Django 5.0.2 on 2024-04-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dp_image',
            field=models.ImageField(null=True, upload_to='media/dp'),
        ),
    ]
