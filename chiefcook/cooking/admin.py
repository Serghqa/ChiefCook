from django.contrib import admin
from cooking.models import Category, Cuisine, Recipe, Ingredient, Tag


class IngredientInline(admin.TabularInline):
    model = Ingredient
    min_num = 1

@admin.register(Category)
class ModelCategory(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Recipe)
class ModelRecipe(admin.ModelAdmin):
    list_display = ["name"]
    list_per_page = 10
    prepopulated_fields = {"slug": ("name",)}
    inlines = [IngredientInline]
    filter_horizontal = ("tags",)
    search_fields = ["name"]
    list_filter = ["author", "category", "cuisine", "tags"]


@admin.register(Cuisine)
class ModelCuisine(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class ModelTag(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}
