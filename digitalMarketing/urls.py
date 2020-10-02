from django.urls import path
import digitalMarketing.views


urlpatterns = [
    path('all', digitalMarketing.views.all_service,
         name='all_services'),
    path('create', digitalMarketing.views.create_DMService, name = 'create_dmservice'),
    path('update/<DMService_id>', digitalMarketing.views.update_DMService, name = 'update_dmservice'),
    path('delete/<DMService_id>', digitalMarketing.views.delete_DMService, name = 'delete_dmservice'),
    path('all-assets', digitalMarketing.views.all_assets,
         name='all_assets'),   
    path('create-daservice', digitalMarketing.views.create_daservice, name = 'create_daservice'),
    path('update-daservice/<DAService_id>', digitalMarketing.views.update_daservice, name = 'update_daservice'),
    path('delete-daservice/<DAService_id>', digitalMarketing.views.delete_daservice, name = 'delete_daservice'),
]