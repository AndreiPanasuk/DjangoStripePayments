from django.conf import settings
from django.views.generic.base import TemplateView, View
from django.http.response import JsonResponse
from rest_framework import permissions, viewsets
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

from .models import Item
from .serializers import ItemSerializer


class ItemView(TemplateView):
    template_name = 'item.html'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        item = Item.objects.get(pk=pk)
        context = self.get_context_data(item=item, **kwargs)
        return self.render_to_response(context)


class CreateSessionView(View):
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
            data = {'session_id': session.id}
        except Exception as e:
            status = 500
            reason = str(e)
            data = {'error': reason}
        return JsonResponse(data, status=status, reason=reason)
    
    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
