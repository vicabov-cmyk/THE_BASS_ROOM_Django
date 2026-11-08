from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),

    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
]