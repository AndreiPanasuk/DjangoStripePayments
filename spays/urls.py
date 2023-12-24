from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'discounts', views.DiscountViewSet)
router.register(r'orders', views.OrderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('item/<int:pk>/', views.ItemView.as_view(), name='item'),
    path('buy/<int:pk>/', views.CreateSessionView.as_view(), name='create-session'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('buy/order/', views.CreateOrderSessionView.as_view(), name='create-order-session'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
