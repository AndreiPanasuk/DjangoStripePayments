from .models import Item, Order, OrderItem, Discount
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'stripe_price_id']


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'name', 'dtype', 'dval']


class OrderItemSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name')
    item_price = serializers.DecimalField(12, 2, source='item.price')
    class Meta:
        model = OrderItem
        fields = ['item_name', 'item_price', 'quantity', 'oisum']
    

class OrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(many=True)
    discounts = DiscountSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'onum', 'odate', 'ouser', 'user_ip', 'osum', 'orderitem_set', 'discounts']
