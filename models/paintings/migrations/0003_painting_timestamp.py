# Generated by Django 2.1 on 2019-02-19 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0002_auto_20190206_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 19, 18, 15, 53, 661375)),
        ),
    ]