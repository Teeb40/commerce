# Generated by Django 5.0.6 on 2024-08-01 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_placed_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placed',
            name='url',
            field=models.ImageField(blank=True, default='No Image', upload_to='images/'),
        ),
    ]
