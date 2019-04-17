from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.diet,name = 'diet'),
    url('^today/$',views.health_of_day,name='healthToday')
]