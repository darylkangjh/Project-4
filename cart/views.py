from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from digitalMarketing.models import DMService, DAService

# Create your views here.


def add_to_dm_cart(request, DMService_id):
    dm_cart = request.session.get('dm_shopping_cart', {})
    
    if DMService_id not in dm_cart:
        dmservice = get_object_or_404(DMService, pk=DMService_id)
        dm_cart[DMService_id] = {
            'id': DMService_id,
            'item_name': dmservice.item_name,
            'price': f"{dmservice.price:.2f}",
        }

        request.session['dm_shopping_cart'] = dm_cart
        messages.success(request,f"{dmservice.item_name} added to cart!")
        return redirect(reverse('all_services'))

    else:
        request.session['dm_shopping_cart'] = cart
        return redirect(reverse('all_services'))

def add_to_da_cart(request, DAService_id):
    da_cart = request.session.get('da_shopping_cart', {})
    if DAService_id not in da_cart: 
        daservice = get_object_or_404(DAService, pk=DAService_id)
        da_cart[DAService_id] ={
            'id': DAService_id,
            'item_name': daservice.item_name,
            'price':f"{daservice.price:.2f}",
            'qty': 1
        }
        request.session["da_shopping_cart"] = da_cart
        messages.success(request,f"{daservice.item_name} added to cart!")
        return redirect(reverse("all_assets"))

    else:
        return redirect(reverse("all_assets"))

def view_cart(request):
    dm_cart = request.session.get('dm_shopping_cart', {})
    da_cart = request.session.get('da_shopping_cart', {})
    total = 0
    
    for key, item in dm_cart.items():
        total += (float(item["price"]))
    
    for key, item in da_cart.items():
        total += (float(item["price"]))  

    return render(request, 'cart/view_cart.template.html', {
        'dm_cart': dm_cart,
        'da_cart':da_cart,
        'total': f"{total:.2f}"
    })
def remove_from_dm_cart(request, DMService_id):
    dm_cart = request.session.get('dm_shopping_cart', {})
    if DMService_id in dm_cart:
        del dm_cart[DMService_id]
        request.session['dm_shopping_cart'] = dm_cart

    return redirect(reverse('view_cart'))

def remove_from_da_cart(request, DAService_id):
    da_cart = request.session.get('da_shopping_cart', {})
    if DAService_id in da_cart:
        del da_cart[DAService_id]
        request.session['da_shopping_cart'] = da_cart
    
    return redirect(reverse('view_cart'))