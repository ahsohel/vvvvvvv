# Generated by Django 3.2.10 on 2022-03-06 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0006_auto_20220306_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationthat_seller_offering_image',
            name='model_Property_and_room_images_2',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='accommodationthat_seller_offering_image',
            name='model_Property_and_room_images_3',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='accommodationthat_seller_offering_image',
            name='model_Property_and_room_images_4',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='accommodationthat_seller_offering_image',
            name='model_Property_and_room_images_5',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]