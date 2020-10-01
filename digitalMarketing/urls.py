from django.urls import path
import digitalMarketing.views

urlpatterns = [
    path('services/all', digitalMarketing.views.all_service,
         name='all_services'),
    path('dmservice/create', digitalMarketing.views.create_DMService, name = 'create_dmservice'),
    path('dmservice/create', digitalMarketing.views.create_DMService, name = 'create_dmservice'),
    path('dmservice/update/<DMService_id>', digitalMarketing.views.update_DMService, name = 'update_dmservice'),
    path('dmservice/delete/<DMService_id>', digitalMarketing.views.delete_DMService, name = 'delete_dmservice'),   
]