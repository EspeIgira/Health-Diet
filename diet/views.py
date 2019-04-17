from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.shortcuts import render


def diet(request):
    return render(request, 'index.html')

def health_of_day(request):
    
    return render(request, 'all-health/today-health.html')