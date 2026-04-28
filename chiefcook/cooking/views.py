from django.http import HttpRequest, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from . models import Recipe, Category, Cuisine, Tag
from . forms import RecipeForm, IngredientFormSet


class IndexView(ListView):
    template_name = "cooking/index.html"
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.select_related("author__user", "category", "cuisine").all()


class CuisineView(ListView):
    template_name = "cooking/cuisine.html"
    context_object_name = "recipes"

    def get_queryset(self):
        slug = self.kwargs["slug"]
        self.cuisine = get_object_or_404(Cuisine, slug=slug)
        return Recipe.objects.select_related(
            "author__user", "category", "cuisine"
        ).filter(cuisine=self.cuisine)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cuisine"] = self.cuisine
        return context


class CategoryView(ListView):
    template_name = "cooking/category.html"
    context_object_name = "recipes"

    def get_queryset(self):
        slug = self.kwargs["slug"]
        self.category = get_object_or_404(Category, slug=slug)
        return Recipe.objects.select_related(
            "author__user", "category", "cuisine"
        ).filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context


class RecipeView(DetailView):
    template_name = "cooking/recipe.html"
    context_object_name = "recipe"

    def get_object(self, queryset=None):
        slug = self.kwargs["slug"]
        recipe = get_object_or_404(
            Recipe.objects.select_related("author__user", "category", "cuisine").prefetch_related("ingredients"),
            slug=slug
        )
        self.category = recipe.category
        self.ingredients = recipe.ingredients.all()
        return recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["ingredients"] = self.ingredients
        return context


class TagView(ListView):
    template_name = "cooking/tag.html"
    context_object_name = "recipes"

    def get_queryset(self):
        slug = self.kwargs["slug"]
        self.tag = get_object_or_404(Tag, slug=slug)
        return Recipe.objects.select_related(
            "author__user", "category", "cuisine"
        ).filter(tags=self.tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context


@login_required
def add_recipe(request: HttpRequest):
    profile = request.user.profile
    if request.method == "POST":
        form_recipe = RecipeForm(request.POST)
        formset = IngredientFormSet(request.POST, prefix="ingredients")
        if form_recipe.is_valid() and formset.is_valid():
            recipe = form_recipe.save(commit=False)

            recipe.author = profile
            recipe.save()
            form_recipe.save_m2m()  # сохранение ManyToMany (tags)
            ingredients = formset.save(commit=False)
            for ingredient in ingredients:
                ingredient.recipe = recipe
                ingredient.save()
            return redirect("cooking:recipe", slug=recipe.slug)
        else:
            non_form_error = formset.non_form_errors() or None

            context = {
                "error_form_ingredient": non_form_error,
                "form_recipe": form_recipe,
                "formset": formset,
            }
            return render(request, "cooking/add_recipe.html", context)

    form_recipe = RecipeForm()
    formset = IngredientFormSet(prefix="ingredients")
    context = {
        "form_recipe": form_recipe,
        "formset": formset,
    }

    return render(request, "cooking/add_recipe.html", context)


def add_ingredient_form(request: HttpRequest):
    # Создаем новую пустую форму для formset
    formset = IngredientFormSet(prefix="ingredients")
    empty_form = formset.empty_form

    context = {
        "form": empty_form,
    }

    return render(request, "cooking/partials/ingredient_form.html", context)
