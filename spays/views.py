import json
from django.conf import settings
from django.views.generic.base import TemplateView, View
from django.http.response import JsonResponse
from rest_framework import permissions, viewsets
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

from .models import Item, Order
from .serializers import ItemSerializer, OrderSerializer


class ItemView(TemplateView):
    template_name = 'item.html'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        item = Item.objects.get(pk=pk)
        context = self.get_context_data(item=item, **kwargs)
        return self.render_to_response(context)

class OrderView(TemplateView):
    template_name = 'order.html'
    
    def get(self, request, *args, **kwargs):
        items = Item.objects.all().order_by('name')
        context = self.get_context_data(items=items, **kwargs)
        return self.render_to_response(context)

class CreateSessionView(View):
    http_method_names = ['get']
    
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        count = request.GET.get('count')
        item = Item.objects.get(pk=pk)
        domain_url = 'http://localhost:8000/'
        reason, status = None, 200
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price': item.stripe_price_id,
                        'quantity': count,
                    },
                ],
                mode='subscription',
                success_url=domain_url + 'success/',
                cancel_url=domain_url + 'cancelled/',
            )
            data = {'session_id': session.id, 'session_url': session.url}
        except Exception as e:
            status = 500
            reason = str(e)
            data = {'error': reason}
        return JsonResponse(data, status=status, reason=reason)
    

class CreateOrderSessionView(View):
    http_method_names = ['post']
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        products = data['products']
        ids = [prod['id'] for prod in products]
        items = dict((item.pk, item) for item in Item.objects.filter(pk__in=ids))
        line_items = []
        for prod in products:
            item = items[prod['id']]
            count = prod['count']
            line_items.append(dict(price=item.stripe_price_id, quantity=count))
        domain_url = 'http://localhost:8000/'
        reason, status = None, 200
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='subscription',
                success_url=domain_url + 'success/',
                cancel_url=domain_url + 'cancelled/',
            )
            data = {'session_id': session.id, 'session_url': session.url}
        except Exception as e:
            status = 500
            reason = str(e)
            data = {'error': reason}
        return JsonResponse(data, status=status, reason=reason)

    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
