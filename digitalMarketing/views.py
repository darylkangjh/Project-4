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


def update_DMService(request, DMService_id):
    if request.method == "POST":
        # 1. retrieve the book that is being updated
        DMService_being_updated = get_object_or_404(DMService, pk=DMService_id)

        # 2. do the modification
        DMServiceForm = DMServiceForm(request.POST, instance=book_being_updated)

        # 3. save if the form is valid
        if book_form.is_valid():
            book_form.save()

            # 4. redirect
            return redirect(reverse(index))
    else:
        # 1. retrieve the book that we are editing
        book_being_updated = get_object_or_404(Book, pk=book_id)

        # 2. create the form containing the existing book's book data
        form = BookForm(instance=book_being_updated)

        # 3. display the form in a template
        return render(request, 'books/update_book.template.html', {
            'form': form
        })



# DAServices Views here
#!!!... Create route for DaServices
def create_DAService(request):
    create_form = DAServiceForm()
    return render(request, 'digitalMarketing/create_daservice.template.html', {
        'form':create_form
    })

# 02. E-Commerce show all products!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

 
