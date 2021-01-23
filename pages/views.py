from django.shortcuts import render
from django.http import HttpResponse

def homeview(request):
    #return HttpResponse('Hello, World! Welcome to the new Greens to Grounds website!')
    return render(request, 'templates/home.html')
