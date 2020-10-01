from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from digitalMarketing.models import DMService

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
        messages.success(request, "Services has been added to your cart!")
        return redirect(reverse('all_services'))

    else:
        request.session['shopping_cart'] = cart
        return redirect(reverse('all_services'))


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