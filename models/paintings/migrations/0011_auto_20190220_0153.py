# Generated by Django 2.1 on 2019-02-20 01:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0010_auto_20190219_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 20, 1, 53, 47, 267052, tzinfo=utc)),
        ),
    ]
