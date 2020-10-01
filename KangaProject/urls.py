from django.contrib import admin
from django.urls import path, include



# remember to name the route's patterns so we can link to navbar!
urlpatterns = [
    # !!!! Indexed on NavBar for all to access
    path('', include('home.urls')),
# -------------------------------------------------------------------
    # !!!! Accessible only if user log in 
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
# -------------------------------------------------------------------   
    # !!!! Accessible only for super user (admin)
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls, name='dashboard'),
    path('products/', include('digitalMarketing.urls')),
    ]