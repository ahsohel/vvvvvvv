# Generated by Django 3.2.10 on 2022-03-06 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0003_alter_listing_of_accommodationthat_seller_offering_model_property_and_room_images_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing_of_accommodationthat_seller_offering',
            name='model_Property_and_room_images_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing_of_accommodationthat_seller_offering',
            name='model_Property_and_room_images_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing_of_accommodationthat_seller_offering',
            name='model_Property_and_room_images_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing_of_accommodationthat_seller_offering',
            name='model_Property_and_room_images_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing_of_accommodationthat_seller_offering',
            name='model_Property_and_room_images_5',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
