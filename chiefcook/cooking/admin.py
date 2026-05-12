from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from cooking.models import Category, Cuisine, Recipe, Ingredient, Tag, User


admin.site.register(User, UserAdmin)


class IngredientInline(admin.TabularInline):
    model = Ingredient
    min_num = 1


@admin.register(Category)
class ModelCategory(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Recipe)
class ModelRecipe(admin.ModelAdmin):
    list_display = ["name", "show_image"]
    list_per_page = 10
    prepopulated_fields = {"slug": ("name",)}
    inlines = [IngredientInline]
    filter_horizontal = ("tags",)
    search_fields = ["name"]
    list_filter = ["author", "category", "cuisine", "tags"]
    save_on_top = True

    @admin.display(description="Изображение")
    def show_image(self, recipe: Recipe):
        if recipe.image:
            return mark_safe(f"<img src='{recipe.image.url}' width=50>")
        return mark_safe('<span style="color: gray;">Нет изображения</span>')


@admin.register(Cuisine)
class ModelCuisine(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class ModelTag(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}
