from django.shortcuts import render, redirect
from .forms import SubscriptionForm

def suscribirse(request):
    if 'cart' not in request.session:
        request.session['cart'] = []

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription_type = form.cleaned_data['subscription_type']
            type_key = subscription_type.split(' ')[0]
            price = {
                'mensual': 2500,
                'semestral': 10000,
                'anual': 25000,
            }[type_key]
            request.session['cart'].append({'type': subscription_type, 'price': price})
            request.session.modified = True
            return redirect('view_cart')
    else:
        form = SubscriptionForm()

    cart_count = len(request.session.get('cart', []))
    return render(request, 'suscripciones/suscribirse.html', {'form': form, 'cart_count': cart_count})

def view_cart(request):
    cart = request.session.get('cart', [])
    total_price = sum(item['price'] for item in cart if isinstance(item, dict))
    cart_count = len(cart)
    return render(request, 'suscripciones/cart.html', {'cart': cart, 'total_price': total_price, 'cart_count': cart_count})

def remove_from_cart(request, index):
    cart = request.session.get('cart', [])
    if index < len(cart):
        del cart[index]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('view_cart')

def index(request):
    cart_count = len(request.session.get('cart', []))
    return render(request, 'index.html', {'cart_count': cart_count})

