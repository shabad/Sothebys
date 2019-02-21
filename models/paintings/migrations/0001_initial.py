# Generated by Django 2.1 on 2019-02-21 01:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=30)),
                ('medium', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 21, 1, 26, 58, 536800, tzinfo=utc))),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Artist')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Seller')),
            ],
        ),
    ]
