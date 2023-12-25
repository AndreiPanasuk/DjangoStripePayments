import json
from decimal import Decimal, getcontext
from django.conf import settings
from django.views.generic.base import View
from django.http.response import JsonResponse
from django.db import transaction
import stripe

from ..models import Item, Order, OrderItem, Discount

stripe.api_key = settings.STRIPE_SECRET_KEY

getcontext().prec = 2
Dec100 = Decimal('100.00')


class CreateSessionView(View):    
    http_method_names = ['get', 'post']
    
    def get(self, request, *args, **kwargs):
        """Create Stripe session for Item"""
        
        pk = kwargs['pk']
        count = request.GET.get('count')
        item = Item.objects.get(pk=pk)
        reason, status = None, 200
        line_items = [
            {
                'price': item.stripe_price_id,
                'quantity': count,
            },
        ]
        try:
            session = self.create_session(request, line_items, coupons=[])
            data = {'session_id': session.id, 'session_url': session.url}
        except Exception as e:
            status = 500
            reason = str(e)
            data = {'error': reason}
        return JsonResponse(data, status=status, reason=reason)
    
    def post(self, request, *args, **kwargs):
        """Create Stripe session for Order"""
        
        data = json.loads(request.body)
        products = data['products']
        ids = [prod['id'] for prod in products]
        items = dict((item.pk, item) for item in Item.objects.filter(pk__in=ids))
        line_items = []
        osum = Decimal('0')
        for prod in products:
            item = items[prod['id']]
            count = Decimal(prod['count'])
            line_items.append(dict(price=item.stripe_price_id, quantity=count))
            osum += Decimal(count * item.price)
        discounts = None
        coupons = []
        if request.user and request.user.is_staff and (discs := data.get('discounts')):
            disc_ids = list(d['id'] for d in discs)
            if disc_ids:
                discounts = list(Discount.objects.filter(pk__in=disc_ids))
                for d in discounts:
                    coupons.append({'coupon': d.stripe_id})
                    if d.dtype == 'Fixed':
                        if osum > d.dval:
                            osum -= d.dval
                        else:
                            osum = Decimal('0')
                    else:
                        osum -= Decimal(osum * d.dval / Dec100)
        reason, status = None, 200
        try:
            session = self.create_session(request, line_items, coupons)
            data = {'session_id': session.id, 'session_url': session.url}
            data['order_id'] = self.create_order(request, osum, products, discounts, items, data)
        except Exception as e:
            status = 500
            reason = str(e)
            data = {'error': reason}
        return JsonResponse(data, status=status, reason=reason)

    def create_session(self, request, line_items, coupons):
        domain_url = request.build_absolute_uri('/')
        return stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            discounts=coupons,
            mode='subscription',
            success_url=domain_url + 'success/',
            cancel_url=domain_url + 'cancelled/',
        )
            
    @transaction.atomic
    def create_order(self, request, osum, products, discounts, items, data):
        ouser = (request.user.username if request.user else '') or 'Anonymous'
        user_ip = request.META.get("REMOTE_ADDR")
        num_cnt = Order.objects.filter(ouser=ouser).count() + 1
        onum = f'{ouser}-{num_cnt}'
        order = Order(
            ouser = ouser,
            user_ip = user_ip,
            onum = onum,
            osum = osum,
            stripe_session_id = data['session_id'],
            stripe_session_url = data['session_url'],
        )
        order.save()
        for prod in products:
            item = items[prod['id']]
            count = Decimal(prod['count'])
            oisum = Decimal(count * item.price)
            oitem = OrderItem(order=order, item=item, quantity=count, oisum=oisum)
            oitem.save()
        if discounts:
            order.discounts.add(*discounts)
        return order.pk
