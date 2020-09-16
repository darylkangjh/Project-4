"""KangaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import digitalMarketing.views
import customer.views

# remember to name the route's patterns so we can link to navbar!
urlpatterns = [
    # !!!! Indexed on NavBar for all to access
    path('', include('home.urls'), name='index'),
    path('services/all', digitalMarketing.views.all_service,
         name='all_services'),

    # path (to sign up)
    # if login in 'logout'. If logout 'login or signup'
# -------------------------------------------------------------------
    # !!!! Accessible only if user log in 
    # path('cart')
    # path('checkout')
    # path('user own page')
# -------------------------------------------------------------------   
    # !!!! Accessible only for super user (admin)
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('all-customer/',  customer.views.allCustomer),
    path('dmservice/create', digitalMarketing.views.create_DMService),
    path('dmservice/update/<DMService_id>', digitalMarketing.views.update_DMService, name = 'update_dmservice'),
    path('daservice/create', digitalMarketing.views.create_DAService)
]
