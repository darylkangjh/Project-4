from django.shortcuts import render, HttpResponse
from .forms import DMServiceForm

# Create your views here.
def create_DMService(request):
    create_form = DMServiceForm()
    return render(request, 'digitalMarketing/create_dmservice.template.html', {
        'form':create_form
    })

# 02. E-Commerce show all products!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

 