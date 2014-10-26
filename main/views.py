from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from main.models import Meal, Rating

class IndexView(generic.ListView):
    template_name = 'main/index.html'
    model = Meal

class MealView(generic.ListView):
    template_name = 'main/meal.html'
    model = Meal

def rating(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    rating = Rating.objects.get(meal=meal_id)
    return render(request, 'main/rating.html', {'meal': meal,'stars':range(0,rating.value)})

def rate(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)

    return render(request,'main/rate.html',{'meal':meal})