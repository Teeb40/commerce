# Generated by Django 5.0.6 on 2024-08-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_bids_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='placed',
            name='current_bid',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='bids',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
