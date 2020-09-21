from django.urls import path
import home.views
urlpatterns = [
    path('', home.views.home, name='index'),
    path('success/',home.views.home, name='login-success')
]