from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.post_list, name='post_list'),

    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('confirm/<str:token>/', views.confirm_subscription, name='confirm_subscription'),
]
