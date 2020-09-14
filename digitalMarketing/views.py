from django.shortcuts import render, HttpResponse
from .forms import DMServiceForm, DAServiceForm

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
def create_DAService(request):
    create_form = DAServiceForm()
    return render(request, 'digitalMarketing/create_daservice.template.html', {
        'form':create_form
    })

# 02. E-Commerce show all products!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

 