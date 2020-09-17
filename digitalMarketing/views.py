from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .forms import DMServiceForm, DAServiceForm
from .models import DMService, DAService

# Create your views here.
# All Views here 

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
        create_form = DMServiceForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(all_service))

        else:
            return render(request, 'digitalMarketing/create_dmservice.template.html', {
                'form': create_form
            })
    
    else:
        create_form = DMServiceForm()
        return render(request, 'digitalMarketing/create_dmservice.template.html', {
            'form': create_form})


def update_DMService(request, DMService_id):
    dm_being_updated = get_object_or_404(DMService, pk=DMService_id)
    if request.method == "POST":
        dmservice_form = DMServiceForm(request.POST, instance=dm_being_updated)
        if dmservice_form.is_valid():
            dmservice_form.save()
            return redirect(reverse(all_service))
        else:
            return render(request, 'digitalMarketing/update_dmservice.template.html', {
            "form": dmservice_form
        })

    else:
        dmservice_form = DMServiceForm(instance=dm_being_updated)
        return render(request, 'digitalMarketing/update_dmservice.template.html',  {
            "form": dmservice_form
        })

def delete_DMService(request, DMService_id):
    dms_to_delete = get_object_or_404(DMService, pk=DMService_id)
    if request.method == 'POST':
        dms_to_delete.delete()
        return redirect(all_service)
    else:
        return render(request, 'digitalMarketing/delete_dmservice.template.html', {
                "DMServices": dms_to_delete
            })

# DAServices Views here
#!!!... Create route for DaServices
def create_DAService(request):
    create_form = DAServiceForm()
    return render(request, 'digitalMarketing/create_daservice.template.html', {
        'form':create_form
    })

# 02. E-Commerce show all products!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

 
