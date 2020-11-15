# pages/urls.py
from django.urls import path
from .views import homeview
from . import views
from pages import views

urlpatterns = [
    path('', views.homeview, name='home'),
]
