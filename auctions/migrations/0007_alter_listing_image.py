# Generated by Django 4.2.2 on 2023-08-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_winner_alter_listing_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.CharField(default='https://boodabike.com/wp-content/uploads/2023/03/no-image.jpg', max_length=1000),
        ),
    ]
