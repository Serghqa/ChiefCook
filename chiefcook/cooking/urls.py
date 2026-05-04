from django.urls import path
from . import views


app_name = "cooking"

urlpatterns = [
     path("", views.IndexView.as_view(), name="index"),
     path("category/<slug:slug>/", views.CategoryView.as_view(), name="category"),
     path("recipe/<slug:slug>/", views.RecipeView.as_view(), name="recipe"),
     path("tag/<slug:slug>/", views.TagView.as_view(), name="tag"),
     path("cuisine/<slug:slug>/", views.CuisineView.as_view(), name="cuisine"),
     path("addrecipe/", views.add_recipe, name="add_recipe"),
     path("add-ingredient-form/", views.add_ingredient_form, name="add_ingredient_form"),
     path("my-recipes/", views.MyRecipesView.as_view(), name="my_recipes"),
]
