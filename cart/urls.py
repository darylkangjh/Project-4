from django.urls import path

from .views import add_to_cart, view_cart, remove_from_cart, update_quantity

urlpatterns = [
    path('add/<DMService_id>', add_to_cart, name='add_to_cart'),
    path('', view_cart, name='view_cart'),
    path('remove/<DMService_id>', remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<DMService_id>',
         update_quantity, name='update_quantity')

]
