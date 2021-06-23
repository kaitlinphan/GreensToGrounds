# pages/urls.py
from django.urls import path
from .views import homeview
from . import views
from pages import views
from django.views.generic.edit import FormView
from .views import OrderFormView, OrderCreateView
from django import forms

urlpatterns = [
    path('', views.homeview, name='home'),
    path('supplier.html', views.homeview, name='supplier'),
    path('orderform', OrderCreateView.as_view(), name='orderform'),
    path('calendar.html', views.calendar_view, name='calendar')
]
