from django.db import models
from django.db.models.manager import Manager


class MealType(models.Model):
    NAME_CHOICES = {
        'first_courses': 'Первые блюда',
        'second_courses': 'Вторые блюда',
        'salads': 'Салаты',
        'desserts': 'Десерты',
    }

    name = models.CharField(max_length=100)
    recipes: Manager['Recipe']

    def get_name_display(self) -> str:
        return self.NAME_CHOICES.get(self.name, 'first_courses')

    def __str__(self) -> str:
        return self.get_name_display()


class Recipe(models.Model):
    name = models.TextField()
    cuisine = models.CharField(max_length=100)
    ingredients = models.JSONField()
    instructions = models.TextField()

    meal_type = models.ForeignKey(
        MealType,
        on_delete=models.CASCADE,
        related_name='recipes',
    )
