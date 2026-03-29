from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import QuerySet

from . models import Recipe, MealType


def index(request: HttpRequest):

    meal_types: QuerySet[MealType] = MealType.objects.all().order_by('id')
    data = {
        'meal_types': meal_types,
    }

    return render(request, 'cooking/index.html', data)


def meal_type(request: HttpRequest, meal_type: str):
    meal_type_obj: MealType = get_object_or_404(
        MealType.objects.prefetch_related('recipes'),
        name=meal_type
    )
    recipes: QuerySet[Recipe] = meal_type_obj.recipes.all()
    data = {
        'meal_type': meal_type_obj,
        'recipes': recipes,
    }
    return render(request, 'cooking/meal_type.html', data)


def recipe(request: HttpRequest, recipe_id: int, slug: str):
    recipe_obj: Recipe = get_object_or_404(
        Recipe.objects.select_related('meal_type'),
        id=recipe_id,
        slug=slug
    )
    meal_type_obj: MealType = recipe_obj.meal_type
    data = {
        'meal_type': meal_type_obj,
        'recipe': recipe_obj,
    }
    return render(request, 'cooking/recipe.html', data)
