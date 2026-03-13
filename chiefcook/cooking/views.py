from django.http import HttpRequest, Http404
from django.shortcuts import render

from .recipes.service import recipes_manager


def index(request: HttpRequest):
    categories = recipes_manager.get_categories()
    data = {
        'categories': categories,
    }

    return render(request, 'cooking/index.html', data)


def category(request: HttpRequest, category: str):
    category_name = recipes_manager.get_category_name(category)
    recipes_by_category = recipes_manager.get_recipes_by_category(category)
    data = {
        'title': category_name,
        'category': category,
        'category_name': category_name,
        'recipes': recipes_by_category,
    }
    return render(request, 'cooking/category.html', data)


def recipe(request: HttpRequest, category: str, recipe_id: int):
    recipe = recipes_manager.get_recipe(category, recipe_id)
    data = {
        'category': category,
        'recipe': recipe,
    }
    return render(request, 'cooking/recipe.html', data)
