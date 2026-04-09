from django.urls import path
from . import views


app_name = "cooking"

urlpatterns = [
     path("", views.index, name="index"),
     path("category/<slug:slug>/", views.category, name="category"),
     path("recipe/<slug:slug>/", views.recipe, name="recipe"),
     path("tag/<slug:slug>/", views.tag, name="tag"),
     path("cuisine/<slug:slug>/", views.cuisine, name="cuisine"),
]
