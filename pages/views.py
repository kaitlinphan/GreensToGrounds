from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django import forms
from . import forms
from .models import LineItem, Product, Order
from .forms import OrderForm, CheckoutForm
from . import cart
from django.contrib import messages

from .models import Order

def homeview(request):
    # return HttpResponse('Hello, World! Welcome to the new Greens to Grounds website!')
    # if Mission.objects.all().count()>0:
    #     mission = Mission.objects.get(pk=1)
    #     context = {"missions" : mission}
    # else:
    #     context = {"missions" : "no mission statement"}
    # return render(request, 'templates/home.html', context)
    return render(request, 'pages/home.html')

def show_cart(request):

    if request.method == 'POST':
        if request.POST.get('submit') == 'Update':
            cart.update_item(request)
            print("UPDATE")
        if request.POST.get('submit') == 'Remove':
            cart.remove_item(request)
            print("REMOVE")

    cart_items = cart.get_all_cart_items(request)
    print(cart_items)
    cart_subtotal = cart.subtotal(request)
    return render(request, 'g2g/cart.html', {
                                            'cart_items': cart_items,
                                            'cart_subtotal': cart_subtotal,
                                            })  


# def place_order(request):
#     form = OrderForm(request.POST)
def order_index_view(request):
    all_products = Product.objects.all()
    return render(request, "g2g/order_index.html", {
        'all_products': all_products
    })

def order_detail_view(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        form = OrderForm(request, request.POST)
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            return redirect('/show_cart')

    form = OrderForm(request, initial={'product_id': product.id})
    return render(request, 'g2g/order_detail.html', {
                                            'product': product,
                                            'form': form,
    })

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            o = Order(
                name = cleaned_data.get('name'),
                email = cleaned_data.get('email'),
                phone_number = cleaned_data.get('phone_number')
            )
            o.save()

            all_items = cart.get_all_cart_items(request)
            for cart_item in all_items:
                li = LineItem(
                    product_id = cart_item.product_id,
                    price = cart_item.price,
                    quantity = cart_item.quantity,
                    order_id = o.id
                )

                li.save()

            cart.clear(request)

            request.session['order_id'] = o.id

            messages.add_message(request, messages.INFO, 'Order Placed!')
            return redirect('checkout')

    else:
        form = CheckoutForm()
        return render(request, 'g2g/checkout.html', {'form': form})                                          

def calendar_view(request):
    return render(request, "pages/calendar.html")

# temporary for navbar
def blog_view(request):
    return render(request, "g2g/blog.html")

def social_view(request):
    return render(request, "g2g/social.html")

def FAQ_view(request):
    return render(request, "g2g/FAQ.html")

def supplier_view(request):
    return render(request, "g2g/supplier.html")

def press_view(request):
    return render(request, "g2g/press.html")
