from django.shortcuts import render, HttpResponse
from .forms import DMServiceForm

# Create your views here.


# DmServices Views here 
# !!! ... Create route for DMServices
def create_DMService(request):
    create_form = DMServiceForm()
    return render(request, 'digitalMarketing/create_dmservice.template.html', {
        'form':create_form
    })


# DAServices Views here
#!!!... Create route for DaServices

# 02. E-Commerce show all products!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

 