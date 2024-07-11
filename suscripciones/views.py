from django.shortcuts import render, redirect
from .forms import SubscriptionForm, UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def suscribirse(request):
    if 'cart' not in request.session:
        request.session['cart'] = []

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription_type = form.cleaned_data['subscription_type']
            price = {
                'Plan Plus: Papel + Digital': 40000,
                'Plan Papel Anual': 32355,
                'Plan Digital Anual': 10800,
            }[subscription_type]
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
    if 0 <= index < len(cart):
        del cart[index]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('view_cart')

def index(request):
    cart_count = len(request.session.get('cart', []))
    return render(request, 'index.html', {'cart_count': cart_count})

def realizar_compra(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            register_form = UserRegistrationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                user.set_password(register_form.cleaned_data['password'])
                user.save()
                login(request, user)
                return redirect('resumen_pedido')
        elif 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('resumen_pedido')
    else:
        register_form = UserRegistrationForm()
        login_form = AuthenticationForm()
    
    return render(request, 'suscripciones/realizar_compra.html', {'register_form': register_form, 'login_form': login_form})

@login_required
def resumen_pedido(request):
    cart = request.session.get('cart', [])
    total_price = sum(item['price'] for item in cart if isinstance(item, dict))
    return render(request, 'suscripciones/resumen_pedido.html', {'cart': cart, 'total_price': total_price})
