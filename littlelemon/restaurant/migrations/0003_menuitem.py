# Generated by Django 4.2.2 on 2023-06-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0002_alter_booking_number_of_guests_alter_menu_inventory"),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("inventory", models.SmallIntegerField()),
            ],
        ),
    ]
