from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),
     path('category/<str:category>', views.category, name='category'),
     path('recipe/<str:category>/<int:recipe_id>', views.recipe, name='recipe'),
]
