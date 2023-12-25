from django.urls import include, path
from rest_framework import routers

from .views import (
    ItemView, OrderView, ItemViewSet, OrderViewSet, DiscountViewSet,
    CreateSessionView
)

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'orders', OrderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('item/<int:pk>/', ItemView.as_view(), name='item'),
    path('buy/<int:pk>/', CreateSessionView.as_view(), name='create-session'),
    path('order/', OrderView.as_view(), name='order'),
    path('buy/order/', CreateSessionView.as_view(), name='create-order-session'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
