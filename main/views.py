from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from main.forms import RateForm

from main.models import Meal, Rating, User


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
    user = get_object_or_404(User, pk=1)
    model = Rating()
    if request.POST:
        model.meal = meal
        model.user = user
        model.value = request.POST.get('value')
        model.comment = request.POST.get('comment')
        model.save()

    form = RateForm()
    return render(request,'main/rate.html',{'meal': meal,'form': form})