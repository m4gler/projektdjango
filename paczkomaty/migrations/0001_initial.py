from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Courier",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=120)),
                ("phone", models.CharField(max_length=20)),
            ],
            options={"ordering": ["full_name"]},
        ),
        migrations.CreateModel(
            name="Locker",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=20, unique=True)),
                ("city", models.CharField(max_length=80)),
                ("address", models.CharField(max_length=160)),
                ("capacity", models.PositiveIntegerField(default=10)),
            ],
            options={"ordering": ["city", "code"]},
        ),
        migrations.CreateModel(
            name="Parcel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("tracking_number", models.CharField(max_length=32, unique=True)),
                ("sender_name", models.CharField(max_length=120)),
                ("recipient_name", models.CharField(max_length=120)),
                ("recipient_phone", models.CharField(max_length=20)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Utworzona"),
                            ("assigned", "Przypisana kurierowi"),
                            ("in_locker", "W paczkomacie"),
                            ("delivered", "Dostarczona"),
                        ],
                        default="created",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "courier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="parcels",
                        to="paczkomaty.courier",
                    ),
                ),
                (
                    "locker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="parcels",
                        to="paczkomaty.locker",
                    ),
                ),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
