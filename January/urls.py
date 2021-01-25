from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('/bods', views.bod_list, name='bod_list'),
    path('/styles', views.style_list, name='style_list'),
    path('/decors', views.decor_list, name='decor_list'),
]

