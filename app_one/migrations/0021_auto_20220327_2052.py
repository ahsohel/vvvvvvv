# Generated by Django 3.2.9 on 2022-03-27 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0020_auto_20220325_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing_of_accommodationthat_seller_offering',
            name='List_create_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 3, 27), null=True),
        ),
        migrations.AlterField(
            model_name='listing_of_accommodationthat_seller_offering',
            name='List_create_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 27, 20, 52, 59, 613728), null=True),
        ),
        migrations.AlterField(
            model_name='user_info_table',
            name='Joined_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 27, 20, 52, 59, 612728)),
        ),
    ]
