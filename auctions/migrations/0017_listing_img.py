# Generated by Django 4.2.2 on 2024-02-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_rename_isactive_listing_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='img',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='listing_images'),
        ),
    ]
