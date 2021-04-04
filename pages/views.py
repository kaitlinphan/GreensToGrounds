from django.shortcuts import render
from django.http import HttpResponse

from .models import Mission

def homeview(request):
    # return HttpResponse('Hello, World! Welcome to the new Greens to Grounds website!')
    # if Mission.objects.all().count()>0:
    #     mission = Mission.objects.get(pk=1)
    #     context = {"missions" : mission}
    # else:
    #     context = {"missions" : "no mission statement"}
    # return render(request, 'templates/home.html', context)
    return render(request, 'templates/home.html')
