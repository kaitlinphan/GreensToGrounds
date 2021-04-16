# pages/urls.py
from django.urls import path
from .views import homeview
from . import views
from pages import views
from django.views.generic.edit import FormView
from pages import OrderFormView

urlpatterns = [
    path('', views.homeview, name='home'),
    path('supplier.html', views.homeview, name='supplier'),
    path('/order', OrderFormView.as_view(), name='orderform'),
]
