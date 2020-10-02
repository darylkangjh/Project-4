from django.urls import path

from .views import add_to_dm_cart, view_cart, remove_from_dm_cart, add_to_da_cart, remove_from_da_cart

urlpatterns = [
    path('add/<DMService_id>', add_to_dm_cart, name='add_to_dm_cart'),
    path('', view_cart, name='view_cart'),
    path('remove/<DMService_id>', remove_from_dm_cart, name='remove_from_dm_cart'),
    path('add-daservice/<DAService_id>', add_to_da_cart, name='add_to_da_cart'),
    path('remove-daservice/<DAService_id>', remove_from_da_cart, name='remove_from_da_cart'),
]
