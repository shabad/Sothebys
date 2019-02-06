# Generated by Django 2.1 on 2019-02-06 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('paintings', '0002_auto_20190206_0159'),
        ('accounts', '0002_auto_20190206_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paintings.Painting'),
        ),
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Seller'),
        ),
    ]
