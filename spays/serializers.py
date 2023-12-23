from .models import Item, Order
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'stripe_price_id']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['onum', 'odate', 'ouser', 'osum', 'items']
