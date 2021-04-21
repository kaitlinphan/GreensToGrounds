from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'produce_box')
    # name = forms.CharField()
    # def place_order(self):
    #     pass