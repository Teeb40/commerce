# Generated by Django 5.0.6 on 2024-09-02 15:17

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_rename_username_bids_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.CharField(default='comment', max_length=100, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AddField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(default='no name', max_length=100, validators=[django.core.validators.MinLengthValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placed',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='winning_bid', to='auctions.comments'),
        ),
    ]
