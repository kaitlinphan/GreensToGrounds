from django.shortcuts import render
from django.http import HttpResponse

from .models import Mission

def homeview(request):
    #return HttpResponse('Hello, World! Welcome to the new Greens to Grounds website!')
    mission = Mission.objects.get(pk=1)
    context = {"missions" : mission}
    return render(request, 'templates/home.html', context)
