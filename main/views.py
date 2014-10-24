from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from main.models import Meal, Rating

class IndexView(generic.ListView):
    template_name = 'main/index.html'
    model = Meal

class RatingView(generic.ListView):
    template_name = 'main/rating.html'
    model = Rating