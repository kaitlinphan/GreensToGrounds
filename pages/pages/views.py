from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import forms
from django.views.generic.edit import FormView, CreateView
from pages.forms import OrderForm

from .models import Mission, Order

def homeview(request):
    # return HttpResponse('Hello, World! Welcome to the new Greens to Grounds website!')
    # if Mission.objects.all().count()>0:
    #     mission = Mission.objects.get(pk=1)
    #     context = {"missions" : mission}
    # else:
    #     context = {"missions" : "no mission statement"}
    # return render(request, 'templates/home.html', context)
    return render(request, 'pages/home.html')


# def place_order(request):
#     form = OrderForm(request.POST)


class OrderFormView(FormView):
    template_name = 'g2g/order_form.html'
    form_class = OrderForm
    success_url = 'orderform'

    def form_valid(self, form):
        form.place_order()
        return super().form_valid(form)

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'g2g/order_form.html'
    # fields = ['name']

    def form_valid(self, form):
        form.place_order()
        return super().form_valid(form)



