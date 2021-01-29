from django import forms
from .models import Food, Bod, Style, Decor

class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ('username', 'photo_url',)

