# Generated by Django 2.2.18 on 2021-03-17 19:53

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0005_create_profiles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 3, 19, 19, 53, 20, 29891, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
    ]
