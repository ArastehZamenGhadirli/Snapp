# Generated by Django 5.1.7 on 2025-04-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("direction", "0002_alter_userdirection_destination_x_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdirection",
            name="initial_amount",
            field=models.FloatField(default=1000000),
        ),
    ]
