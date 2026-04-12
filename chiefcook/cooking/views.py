from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import QuerySet

from . models import Recipe, Category, Cuisine, Ingredient, Tag


def index(request: HttpRequest):
    recipes: QuerySet[Recipe] = Recipe.objects.select_related("author__user", "category", "cuisine").all()
    context = {
        "recipes": recipes,
    }

    return render(request, "cooking/index.html", context)


def cuisine(request: HttpRequest, slug: str):
    cuisine: Cuisine = get_object_or_404(Cuisine, slug=slug)
    recipes: QuerySet[Recipe] = Recipe.objects.select_related(
        "author__user", "category", "cuisine"
    ).filter(cuisine=cuisine)
    context = {
        "recipes": recipes,
        "cuisine": cuisine,
    }

    return render(request, "cooking/cuisine.html", context)


def category(request: HttpRequest, slug: str):
    category: Category = get_object_or_404(Category, slug=slug)
    recipes: QuerySet[Recipe] = Recipe.objects.select_related(
        "author__user", "category", "cuisine"
    ).filter(category=category)
    context = {
        "category": category,
        "recipes": recipes,
    }

    return render(request, "cooking/category.html", context)


def recipe(request: HttpRequest, slug: str):
    recipe: Recipe = get_object_or_404(
        Recipe.objects.select_related("author__user", "category", "cuisine").prefetch_related("ingredients"),
        slug=slug
    )
    category: Category = recipe.category
    ingredients: QuerySet[Ingredient] = recipe.ingredients.all()
    context = {
        "recipe": recipe,
        "category": category,
        "ingredients": ingredients,
    }

    return render(request, "cooking/recipe.html", context)

def tag(request: HttpRequest, slug: str):
    tag: Tag = get_object_or_404(Tag, slug=slug)
    recipes: QuerySet[Recipe] = Recipe.objects.select_related(
        "author__user", "category", "cuisine"
    ).filter(tags=tag)
    context = {
        "tag": tag,
        "recipes": recipes,
    }

    return render(request, "cooking/tag.html", context)
