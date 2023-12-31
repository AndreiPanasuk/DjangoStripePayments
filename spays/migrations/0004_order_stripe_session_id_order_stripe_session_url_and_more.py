# Generated by Django 4.2.8 on 2023-12-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("spays", "0003_order_orderitem_order_items"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="stripe_session_id",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="order",
            name="stripe_session_url",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="order",
            name="user_ip",
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
