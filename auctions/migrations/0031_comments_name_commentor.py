# Generated by Django 5.0.6 on 2024-09-02 20:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_alter_comments_id_alter_comments_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='name_commentor',
            field=models.CharField(default='nothing', max_length=100, validators=[django.core.validators.MinLengthValidator(1)]),
            preserve_default=False,
        ),
    ]
