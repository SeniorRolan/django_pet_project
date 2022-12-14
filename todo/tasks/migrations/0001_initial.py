# Generated by Django 4.1.3 on 2022-11-21 22:50

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TruckModel",
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
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "side_number",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Бортовой номер"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название модели"),
                ),
                (
                    "load_capacity",
                    models.SmallIntegerField(
                        null=True, verbose_name="Грузоподъёмность"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Truck",
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
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "current_cargo",
                    models.SmallIntegerField(
                        null=True, verbose_name="Текущая загруженность"
                    ),
                ),
                (
                    "overload",
                    models.SmallIntegerField(
                        null=True, verbose_name="Перегруженность в процентах"
                    ),
                ),
                ("truck_model", models.ManyToManyField(to="tasks.truckmodel")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
