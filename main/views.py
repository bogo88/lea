from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from main.models import Meal, Rating


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    model = Meal


class MealsView(generic.ListView):
    template_name = 'main/meals.html'
    model = Meal


def rating(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    try:
        ratings = Rating.objects.filter(meal=meal_id)
        return render(request, 'main/rating.html', {'meal': meal, 'ratings': ratings})
    except Rating.DoesNotExist:
        return render(request, 'main/rating.html', {'meal': meal})


def rate(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)

    return render(request,'main/rate.html',{'meal':meal})