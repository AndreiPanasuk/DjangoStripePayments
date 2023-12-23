# Generated by Django 4.2.8 on 2023-12-23 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("spays", "0002_item_stripe_price_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("odate", models.DateTimeField(auto_now_add=True)),
                ("ouser", models.CharField(max_length=100)),
                ("onum", models.CharField(blank=True, max_length=100)),
                ("osum", models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.DecimalField(decimal_places=2, max_digits=12)),
                ("oisum", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="spays.item"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="spays.order"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="items",
            field=models.ManyToManyField(through="spays.OrderItem", to="spays.item"),
        ),
    ]