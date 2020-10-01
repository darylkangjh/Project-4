from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
import os
from django.conf import settings
import stripe
from digitalMarketing.models import DMService
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Purchase
from django.contrib.auth.decorators import login_required
endpoint_secret = os.environ.get('endpoint_secret')

# Create your views here.

# --------------------------------------------(Stripe code here)----------------------------------------
def checkout_success(request):
    # Empty the shopping cart
    request.session['shopping_cart'] = {}
    return HttpResponse("Checkout success")

def checkout_cancelled(request):
    # Empty the shopping cart
    request.session['shopping_cart'] = {}
    return HttpResponse("Checkout cancelled")

@login_required
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('shopping_cart', {})

    # create our line items
    line_items = []
    all_item_ids = []

    # go through each book in the shopping cart
    for DMService_id, dmservice in cart.items():
        # retrieve the book by its id from the database
        DMService_model = get_object_or_404(DMService, pk=DMService_id)
        # Line item here
        item = {
            "name": DMService_model.item_name,
            "amount": int(DMService_model.price * 100),
            "quantity": 1,
            "currency": "sgd",
        }

        line_items.append(item)
        all_item_ids.append(str(DMService_model.id))

    # get the current website
    current_site = Site.objects.get_current()

    # get the domain name
    domain = current_site.domain
    
    # create a payment session to represent the current transaction
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],  # take credit cards
        line_items=line_items,
        client_reference_id=request.user.id,
        metadata={
            "all_item_ids": ",".join(all_item_ids)
        },
        mode="payment",
        success_url=domain + reverse("checkout_success"),
        cancel_url=domain + reverse("checkout_cancelled")
    )

    return render(request, "checkout/checkout.template.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })


@csrf_exempt
def payment_completed(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

    # Fulfill the purchase...
    handle_payment(session)

  return HttpResponse(status=200)

def handle_payment(session):
    # print(session)
    user = get_object_or_404(User, pk=session["client_reference_id"])


    # change the metadata from string back to array
    all_item_ids = session["metadata"]["all_item_ids"].split(",")


    for DMService_id in all_item_ids:
        DMService_model = get_object_or_404(DMService, pk=DMService_id)

        # create the purchase model
        purchase = Purchase()
        purchase.DMService_id = DMService_model
        purchase.user_id = user
        purchase.save()