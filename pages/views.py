from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import forms
from django.views.generic.edit import FormView
from .forms import OrderForm

from .models import Mission

def homeview(request):
    # return HttpResponse('Hello, World! Welcome to the new Greens to Grounds website!')
    # if Mission.objects.all().count()>0:
    #     mission = Mission.objects.get(pk=1)
    #     context = {"missions" : mission}
    # else:
    #     context = {"missions" : "no mission statement"}
    # return render(request, 'templates/home.html', context)
    return render(request, 'pages/home.html')


# class OrderForm(forms.Form):
#     name = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea)

#     def place_order(self):
#         pass

class OrderFormView(FormView):
    template_name = 'g2g/orderform.html'
    form_class = OrderForm
    success_url = '/order'

    def form_valid(self, form):
        form.place_order()
        return super().form_valid(form)



