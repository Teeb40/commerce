# Generated by Django 5.0.6 on 2024-08-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bids_comments_placed'),
    ]

    operations = [
        migrations.AddField(
            model_name='placed',
            name='url',
            field=models.URLField(default='No Photo'),
            preserve_default=False,
        ),
    ]
