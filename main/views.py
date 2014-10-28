from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from main.forms import RateForm, LoginForm
from datetime import datetime
from django.db.models import Avg
from django.contrib import messages
from main.models import Meal, Rating, User
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    model = Meal


class MealsView(generic.ListView):
    template_name = 'main/meals.html'
    model = Meal


def profile(request):
    form = LoginForm()
    if request.POST:
        try:
            log_out = request.POST['logout']
        except MultiValueDictKeyError:
            log_out = False
        if log_out:
            logout(request)
            messages.success(request, 'Loged out')
            return redirect('main:index')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Welcome '+username)
                return redirect('main:index')
            else:
                messages.warning(request, 'Your account is disabled')
        else:
            messages.warning(request, 'Wrong username or password')
    return render(request, 'main/profile.html', {'form': form})


def rating(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    try:
        ratings = Rating.objects.filter(meal=meal_id).order_by('-rate_date')
        avg_rating = meal.rating_set.aggregate(Avg('value'))
        if avg_rating['value__avg'] > 0:
            avg_value = avg_rating['value__avg']
        else:
            avg_value = 0
        avg_stars = range(0, int(avg_value))
        half_star = avg_value - int(avg_value)
        return render(request, 'main/rating.html',
                      {'meal': meal,
                       'ratings': ratings,
                       'avg_rating': avg_rating,
                       'avg_stars': avg_stars,
                       'half_star': half_star})
    except Rating.DoesNotExist:
        return render(request, 'main/rating.html', {'meal': meal})


def rate(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    user = get_object_or_404(User, pk=request.user.id)
    model = Rating()
    if request.POST:
        if request.POST.get('value'):
            model.meal = meal
            model.user = user
            model.rate_date = datetime.now()
            model.value = request.POST.get('value')
            model.comment = request.POST.get('comment')
            model.save()
            return redirect('main:rating', meal_id)
        else:
            messages.warning(request, 'You have to select rating')

    form = RateForm()
    return render(request,'main/rate.html',{'meal': meal,'form': form})