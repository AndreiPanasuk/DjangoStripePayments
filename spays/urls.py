from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'items-list', views.ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('item/<int:pk>/', views.ItemView.as_view(), name='item'),
    path('buy/<int:pk>/', views.CreateSessionView.as_view(), name='create-session'),
    path('data/items/', views.ItemList.as_view(), name='items-list'),
    path('data/item/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
