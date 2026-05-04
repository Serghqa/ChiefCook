from django.http import HttpRequest, Http404
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from . models import Profile, Recipe, Category, Cuisine, Tag
from . forms import RecipeForm, IngredientFormSet
from . utils import RecipeQuerysetMixin, FilteredQuerysetMixin


class IndexView(RecipeQuerysetMixin, ListView):
    template_name = "cooking/index.html"
    context_object_name = "recipes"


class CuisineView(FilteredQuerysetMixin, ListView):
    template_name = "cooking/cuisine.html"
    context_object_name = "recipes"
    filter_model = Cuisine
    filter_field = "cuisine"
    context_name = "cuisine"


class CategoryView(FilteredQuerysetMixin, ListView):
    template_name = "cooking/category.html"
    context_object_name = "recipes"
    filter_model = Category
    filter_field = "category"
    context_name = "category"


class TagView(FilteredQuerysetMixin, ListView):
    template_name = "cooking/tag.html"
    context_object_name = "recipes"
    filter_model = Tag
    filter_field = "tags"
    context_name = "tag"


class MyRecipesView(RecipeQuerysetMixin, ListView):
    template_name = "cooking/index.html"
    context_object_name = "recipes"

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(author=user.profile)


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
