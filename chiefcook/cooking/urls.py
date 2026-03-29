from django.urls import path
from . import views


app_name = 'cooking'

urlpatterns = [
     path('', views.index, name='index'),
     path('category/<str:meal_type>/', views.meal_type, name='meal_type'),
     path('recipe/<int:recipe_id>/<slug:slug>/', views.recipe, name='recipe'),
]
