from django.conf.urls import patterns, url
from main.models import Meal, Rating
from main import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^rating/(?P<meal_id>[0-9]+)',views.rating, name='rating'),
    url(r'^rate/(?P<meal_id>[0-9]+)',views.rate, name='rate'),
    url(r'^meals',views.MealsView.as_view(
	model = Meal,
	context_object_name="all_meals",
    ), name='meals'),
)