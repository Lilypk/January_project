from django.shortcuts import render, redirect
from .models import Food, Bod, Style, Decor
from .forms import FoodForm
# Create your views here.

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'January/food_list.html', {'foods': foods})

def bod_list(request):
    bods = Bod.objects.all()
    return render(request, 'January/bod_list.html', {'bods': bods})

def style_list(request):
    styles = Style.objects.all()
    return render(request, 'January/style_list.html', {'styles': styles})

def decor_list(request):
    decors = Decor.objects.all()
    return render(request, 'January/decor_list.html', {'decors': decors})

