# Generated by Django 4.2.2 on 2023-06-21 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_date_alter_message_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 21, 5, 31, 6, 312926)),
        ),
    ]