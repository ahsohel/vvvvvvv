# Generated by Django 3.2.9 on 2022-03-25 06:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0011_user_info_table_joined_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing_of_accommodationthat_seller_offering',
            name='link_with_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_one.user_info_table'),
        ),
        migrations.AlterField(
            model_name='user_info_table',
            name='Joined_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 25, 12, 59, 26, 652726)),
        ),
    ]