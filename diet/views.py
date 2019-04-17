from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.shortcuts import render
from .models import Image,Category,Comment


def diet(request):
    diets = Image.objects.filter() 
    return render(request, 'index.html',{"diets":diets})

def health_of_day(request):

    diets = Image.todays_diet () 
    return render(request, 'all-health/today-health.html',{"diets":diets})


def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-health/image.html", {"image":image})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        name = request.GET.get("category")
        searched_categories = Image.search_by_category(name)
        message = f"{name}"

        return render(request, 'all-images/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})

