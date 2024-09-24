# Generated by Django 5.0.2 on 2024-09-20 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='Description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='booking',
            name='BookingDate',
            field=models.DateField(default='2024-09-20'),
        ),
    ]
