from django.shortcuts import render, HttpResponse, redirect, reverse
from .forms import DMServiceForm, DAServiceForm
from .models import DMService, DAService

# Create your views here.
# DmServices Views here 


def all_service(request):

    DMServices = DMService.objects.all()
    DAServices = DAService.objects.all()
    return render(request, 'digitalMarketing/all_services.template.html', {
        'DMServices': DMServices,
        'DAServices': DAServices
    })


# !!! ... Create route for DMServices
def create_DMService(request):
    if request.method == 'POST':
        create_form = DMServiceForm()

        if create_form.is_valid():
            return redirect(reverse(all_services))

        else:
            return render(request, 'digitalMarketing/create_dmservice.template.html', {
            'form': create_form
        })
    
    else:
        create_form = DMServiceForm()
        return render(request, 'digitalMarketing/create_dmservice.template.html', {
            'form': create_form})


# DAServices Views here
#!!!... Create route for DaServices
def create_DAService(request):
    create_form = DAServiceForm()
    return render(request, 'digitalMarketing/create_daservice.template.html', {
        'form':create_form
    })

# 02. E-Commerce show all products!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

 
