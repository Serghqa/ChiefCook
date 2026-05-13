from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Recipe, Tag, Ingredient, Category, Cuisine


from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError

class BaseIngredientFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

    def clean(self):
        super().clean()

        count_form_errors = sum(1 for err in self.errors if err)
        if count_form_errors:
            if not any(form.has_changed() for form in self.forms):
                raise ValidationError("Добавьте хотя бы один ингредиент.")

            raise ValidationError("Заполните обязательные поля ингредиентов.")



class RecipeForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "tag-field"}),
        label="Теги"
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "r-select-field"}),
        label="Категория",
        empty_label="Выберите категорию",
    )
    cuisine = forms.ModelChoiceField(
        queryset=Cuisine.objects.all(),
        widget=forms.Select(attrs={"class": "r-select-field"}),
        label="Кухня",
        empty_label="Выберите кухню",
    )

    class Meta:
        model = Recipe
        fields = ["name", "category", "cuisine", "tags", "image", "description", "instructions", "cooking_time"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "r-name-field",
                    "placeholder": "Название рецепта...",
                    "autocomplete": "off",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "r-file-field",
                    "accept": "image/*",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "r-text-field",
                    "rows": 3,
                    "placeholder": "Краткое описание...",
                }
            ),
            "instructions": forms.Textarea(
                attrs={
                    "class": "r-text-field",
                    "rows": 8,
                    "placeholder": "Пошаговый процесс...",
                }
            ),
            "cooking_time": forms.NumberInput(
                attrs={
                    "class": "r-time-field",
                    "placeholder": "Минуты...",
                }
            ),
        }


class IngredientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unit'].required = False

    class Meta:
        model = Ingredient
        fields=["name", "amount", "unit"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "i-name-field",
                    "placeholder": "Название ингредиента...",
                }
            ),
            "amount": forms.NumberInput(
                attrs={
                    "class": "i-amount-field",
                    "step": "0.1",
                    "min": "0",
                    "placeholder": "Количество...",
                }
            ),
            "unit": forms.Select(
                attrs={
                    "class": "i-unit-field",
                }
            ),
        }


IngredientFormSet = inlineformset_factory(
    Recipe,  # родительская модель
    Ingredient,  # дочерняя модель
    form=IngredientForm,
    formset=BaseIngredientFormSet,
    extra=2,  # количество пустых форм для добавления ингредиентов
    can_delete=False,  # возможность удалить строку
    can_delete_extra=True,
)
