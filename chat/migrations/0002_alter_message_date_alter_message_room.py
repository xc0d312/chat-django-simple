# Generated by Django 4.2.2 on 2023-06-21 03:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 21, 3, 33, 1, 455148)),
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=1000000),
        ),
    ]