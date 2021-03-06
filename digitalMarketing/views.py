from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .forms import DMServiceForm, DAServiceForm, SearchForm, DASearchForm
from .models import DMService, DAService
from django.contrib import messages
from django.db.models import Q


# --------------------------------------------------(Digital Marketing Services)
# All Views here 

def all_service(request):
    
    DMServices = DMService.objects.all()
    queries = ~Q(pk__in=[])

    if request.GET:
            # if a title is specified, add it to the query
            if 'item_name' in request.GET and request.GET['item_name']:
                queries = queries & Q(item_name__icontains=request.GET['item_name'])

            # if a genre is specified, add it to the query
            if 'category' in request.GET and request.GET['category']:
                queries = queries & Q(category__in=request.GET['category'])


    allDmservices=DMServices.filter(queries)
    search_form=SearchForm()

    # DAServices = DAService.objects.all()
    return render(request, 'digitalMarketing/all_services.template.html', {
        'allDmservices': allDmservices,
        'search_form': search_form,
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
        if request.user.is_superuser:
            dmservice_form = DMServiceForm(instance=dm_being_updated)
            return render(request, 'digitalMarketing/update_dmservice.template.html',  {
                "form": dmservice_form
            })
        else:
            return render(request, 'digitalMarketing/update_dmservice.template.html', {
            "form": dmservice_form
        })

def delete_DMService(request, DMService_id):
    dms_to_delete = get_object_or_404(DMService, pk=DMService_id)
    if request.method == 'POST':
        dms_to_delete.delete()
        return redirect(all_service)
    else:
        if request.user.is_superuser:
            return render(request, 'digitalMarketing/delete_dmservice.template.html', {
                    "DMServices": dms_to_delete
                })

        else:
            return redirect(reverse(all_assets))

# --------------------------------------------------(Digital Assets)
def all_assets(request):
    
    all_daservices = DAService.objects.all()
    queries = ~Q(pk__in=[])

    if request.GET:
            # if a title is specified, add it to the query
            if 'item_name' in request.GET and request.GET['item_name']:
                queries = queries & Q(item_name__icontains=request.GET['item_name'])

            # if a genre is specified, add it to the query
            if 'category' in request.GET and request.GET['category']:
                queries = queries & Q(category__in=request.GET['category'])


    all_daservices = all_daservices.filter(queries)
    search_form=DASearchForm()
    # DAServices = DAService.objects.all()
    return render(request, 'digitalMarketing/all_assets.template.html', {
        'all_daservices': all_daservices,
        'search_form': search_form,
    })

def create_daservice(request):

    if request.method == "POST":
        create_form = DAServiceForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, f"{create_form.cleaned_data['item_name']} has been created")
            return redirect(reverse(all_assets))
        else:
                return render(request, "digitalMarketing/create_daservice.template.html",{
                "form": create_form
            })
    else:
        create_form = DAServiceForm()
        return render(request, "digitalMarketing/create_daservice.template.html",{
                "form": create_form
            })

def update_daservice(request, DAService_id):
    daservice_to_update = get_object_or_404(DAService, pk=DAService_id)
    if request.method == "POST":
        update_form = DAServiceForm(request.POST, instance=daservice_to_update)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, f"{update_form.cleaned_data['item_name']} has been updated")
            return redirect(reverse(all_assets))
        else:
            return render(request, 'digitalMarketing/update_daservice.template.html', {
            "form": update_form
        })

    else:
        if request.user.is_superuser:
            update_form = DAServiceForm(instance=daservice_to_update)
            return render(request, 'digitalMarketing/update_daservice.template.html',  {
                "form": update_form
            })
        else:
            return redirect(reverse(all_assets))

def delete_daservice(request, DAService_id):
    das_to_delete = get_object_or_404(DAService, pk=DAService_id)
    if request.method == 'POST':
        das_to_delete.delete()
        return redirect(all_assets)
    else:
        if request.user.is_superuser:
            return render(request, 'digitalMarketing/delete_daservice.template.html', {
                    "daservices": das_to_delete
                })

        else:
            return redirect(reverse(all_assets))