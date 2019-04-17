from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
    url('^$',views.diet,name = 'diet'),
    url('^$',views.health_of_day,name='healthToday'),  
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^vegetable/',views.vegetable,name ='vegetable'),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)