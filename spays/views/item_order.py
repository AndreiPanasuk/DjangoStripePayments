from django.conf import settings
from django.views.generic.base import TemplateView
from rest_framework import permissions, viewsets

from ..models import Item, Order, Discount
from ..serializers import ItemSerializer, OrderSerializer, DiscountSerializer


class ItemView(TemplateView):
    template_name = 'item.html'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        item = Item.objects.get(pk=pk)
        context = self.get_context_data(
            item=item, 
            STRIPE_PUBLISHABLE_KEY=settings.STRIPE_PUBLISHABLE_KEY,
            **kwargs,
        )
        return self.render_to_response(context)


class OrderView(TemplateView):
    template_name = 'order.html'
    
    def get(self, request, *args, **kwargs):
        items = Item.objects.all().order_by('name')
        if request.user and request.user.is_staff:
            discounts = Discount.objects.all().order_by('name')
        else:
            discounts = None
        context = self.get_context_data(
            items=items, 
            discounts=discounts, 
            STRIPE_PUBLISHABLE_KEY=settings.STRIPE_PUBLISHABLE_KEY,
            **kwargs,
        )
        return self.render_to_response(context)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAdminUser]


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all().order_by('id')
    serializer_class = DiscountSerializer
    permission_classes = [permissions.IsAdminUser]

