from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from digitalMarketing.models import DMService, DAService

# Create your views here.


def add_to_cart(request, DMService_id):
    cart = request.session.get('shopping_cart', {})
    
    if DMService_id not in cart:
        dmservice = get_object_or_404(DMService, pk=DMService_id)
        cart[DMService_id] = {
            'id': DMService_id,
            'item_name': dmservice.item_name,
            'price': f"{dmservice.price:.2f}",
        }

        request.session['shopping_cart'] = cart
        messages.success(request,f"{dmservice.item_name} added to cart!")
        return redirect(reverse('all_services'))

    else:
        request.session['shopping_cart'] = cart
        return redirect(reverse('all_services'))

def add_to_dacart(request, DAService_id):
    cart = request.session.get('shopping_cart', {})
    if DAService_id not in cart: 
        daservice = get_object_or_404(DAService, pk=DAService_id)
        cart[DAService_id] ={
            'id': DAService_id,
            'item_name': daservice.item_name,
            'price':f"{daservice.price:.2f}",
            'qty': 1
        }
        request.session["shopping_cart"] = cart
        messages.success(request,f"{daservice.item_name} added to cart!")
        return redirect(reverse("all_assets"))

    else: 
        cart[DAService_id]["qty"] += 1
        request.session["shopping_cart"] =cart
        return redirect(reverse("all_assets"))

def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    total = 0

    for key, item in cart.items():
        total += (float(item["price"])) 
    
    return render(request, 'cart/view_cart.template.html', {
        'shopping_cart': cart,
        'total': f"{total:.2f}"
    })

def remove_from_cart(request, DMService_id):
    cart = request.session.get('shopping_cart', {})

    if DMService_id in cart:
        del cart[DMService_id]
        request.session['shopping_cart'] = cart

    return redirect(reverse('view_cart'))