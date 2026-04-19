from django.urls import path
from . import views


app_name = "cooking"

urlpatterns = [
     path("", views.index, name="index"),
     path("category/<slug:slug>/", views.category, name="category"),
     path("recipe/<slug:slug>/", views.recipe, name="recipe"),
     path("tag/<slug:slug>/", views.tag, name="tag"),
     path("cuisine/<slug:slug>/", views.cuisine, name="cuisine"),
     path("addrecipe/", views.add_recipe, name="add_recipe"),
     path("add-ingredient-form/", views.add_ingredient_form, name="add_ingredient_form"),
]
