from django.urls import path
from . import views

app_name = 'bassroom'

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('artists/', views.artists, name='artists'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]
