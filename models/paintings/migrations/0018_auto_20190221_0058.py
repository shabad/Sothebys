# Generated by Django 2.1 on 2019-02-21 00:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0017_auto_20190221_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 21, 0, 58, 53, 776183, tzinfo=utc)),
        ),
    ]
