from django.shortcuts import render

# Create your views here.


def allCustomer(request):
    return render(request, 'customer/all-customer.template.html')
