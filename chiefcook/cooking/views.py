from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import QuerySet

from . models import Recipe, MealType


def index(request: HttpRequest):

    categories: QuerySet[MealType] = MealType.objects.all().order_by('id')
    data = {
        'categories': categories,
    }

    return render(request, 'cooking/index.html', data)


def category(request: HttpRequest, category: str):
    meal_type = MealType.objects.prefetch_related('recipes').get(name=category)
    recipes: QuerySet[Recipe] = meal_type.recipes.all()
    data = {
        'meal_type': meal_type,
        'recipes': recipes,
    }
    return render(request, 'cooking/category.html', data)


def recipe(request: HttpRequest, category: str, recipe_id: int):
    recipe = Recipe.objects.select_related('meal_type').get(id=recipe_id)
    meal_type = recipe.meal_type
    data = {
        'meal_type': meal_type,
        'recipe': recipe,
    }
    return render(request, 'cooking/recipe.html', data)
