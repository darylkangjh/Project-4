def cart_contents(request):

    da_cart=request.session.get("da_shopping_cart", {})
    dm_cart=request.session.get("dm_shopping_cart", {})
    

    return {
        'da_shopping_cart':da_cart,
        'dm_shopping_cart':dm_cart,
        'number_of_items':len(dm_cart) + len(da_cart)
    }