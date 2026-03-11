from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .recipes.service import recipes_manager


def index(request: HttpRequest) -> HttpResponse:
    categories = recipes_manager.get_categories()
    data = {
        'categories': categories,
    }

    return render(request, 'cooking/index.html', data)


def category(request: HttpRequest, category) -> HttpResponse:
    category_name = recipes_manager.get_category_name(category)
    recipes_by_category = recipes_manager.get_recipes_by_category(category)
    data = {
        'title': category_name,
        'category_name': category_name,
        'recipes': recipes_by_category,
    }
    return render(request, 'cooking/category.html', data)
