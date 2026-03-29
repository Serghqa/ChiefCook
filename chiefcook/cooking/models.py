from django.db import models
from django.db.models.manager import Manager
from django.urls import reverse


class MealType(models.Model):
    NAME_CHOICES = {
        'first_courses': 'Первые блюда',
        'second_courses': 'Вторые блюда',
        'salads': 'Салаты',
        'desserts': 'Десерты',
    }

    name = models.CharField(max_length=100, unique=True,)
    recipes: Manager['Recipe']

    def get_name_display(self) -> str:
        return self.NAME_CHOICES.get(self.name, '')

    def get_absolute_url(self):
        return reverse('cooking:meal_type', kwargs={'meal_type': self.name})

    def __str__(self) -> str:
        return self.get_name_display()


class Recipe(models.Model):
    name = models.CharField(max_length=300)
    cuisine = models.CharField(max_length=100)
    ingredients = models.JSONField()
    instructions = models.TextField()
    slug = models.SlugField(max_length=255)

    meal_type = models.ForeignKey(
        MealType,
        on_delete=models.CASCADE,
        related_name='recipes',
    )

    def get_absolute_url(self):
        return reverse('cooking:recipe', kwargs={'recipe_id': self.pk, 'slug': self.slug})
