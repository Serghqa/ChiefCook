from typing import Any

from django import forms
from django.forms import inlineformset_factory

from .models import Recipe, Tag, Ingredient, Category, Cuisine


class RecipeForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "tag-grid"}),
        required=False,
        label="Теги"
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(),
        label="Категория",
        empty_label="Выберите категорию",
    )
    cuisine = forms.ModelChoiceField(
        queryset=Cuisine.objects.all(),
        widget=forms.Select(),
        label="Кухня",
        empty_label="Выберите кухню",
    )
    class Meta:
        model = Recipe
        fields = ["name", "category", "cuisine", "tags", "description", "instructions", "cooking_time"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Введите название рецепта...",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Краткое описание...",
                }
            ),
            "instructions": forms.Textarea(
                attrs={
                    "rows": 8,
                    "placeholder": "Пошаговый процесс...",
                }
            ),
            "cooking_time": forms.NumberInput(
                attrs={
                    "placeholder": "Минуты",
                }
            ),
        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields=["name", "amount", "unit"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Введите название ингредиента",
                }
            ),
            "amount": forms.NumberInput(
                attrs={
                    "step": "0.1",
                    "min": "0",
                }
            ),
            "unit": forms.Select(),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        print(name)
        return name


IngredientFormSet = inlineformset_factory(
    Recipe,  # родительская модель
    Ingredient,  # дочерняя модель
    form=IngredientForm,
    extra=1,  # количество пустых форм для добавления ингредиентов
    can_delete=False,  # возможность удалить строку
    can_delete_extra=True,
)
