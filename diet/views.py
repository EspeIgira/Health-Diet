from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render


def diet(request):
    return render(request, 'index.html'))

def health_of_day(request):
    
    return render(request, 'all-heath/today-health.html')
