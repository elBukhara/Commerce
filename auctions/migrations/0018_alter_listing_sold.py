# Generated by Django 4.2.2 on 2024-02-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_listing_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sold',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
