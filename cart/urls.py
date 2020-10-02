from django.urls import path

from .views import add_to_cart, view_cart, remove_from_cart, add_to_dacart

urlpatterns = [
    path('add/<DMService_id>', add_to_cart, name='add_to_cart'),
    path('', view_cart, name='view_cart'),
    path('remove/<DMService_id>', remove_from_cart, name='remove_from_cart'),
    path('add-daservice/<DAService_id>', add_to_dacart, name='add_to_dacart'),
]
