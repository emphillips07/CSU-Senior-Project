# Generated by Django 4.2 on 2024-04-14 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_alter_reservation_arrival_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='isCancelled',
            field=models.BooleanField(default=False),
        ),
    ]