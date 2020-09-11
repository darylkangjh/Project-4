from django.urls import path
import customer.views
urlpatterns = [
    path('all-customer/', customer.views.customer)
]