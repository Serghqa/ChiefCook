from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify as django_slugify
from transliterate import slugify as trans_slugify

from django.db import models

def unique_slugify(text):
    return trans_slugify(text) or django_slugify(text) or "n-a"

class Category(models.Model):
    class CategoryChoices(models.TextChoices):
        BREAKFAST = 'BREAKFAST', 'Завтраки'
        FIRST_COURSE = 'FIRST_COURSE', 'Первые блюда'
        SECOND_COURSE = 'SECOND_COURSE', 'Вторые блюда'
        SALAD = 'SALAD', 'Салаты'
        SNACK = 'SNACK', 'Закуски'
        DESSERT = 'DESSERT', 'Десерты и выпечка'
        DRINK = 'DRINK', 'Напитки'
        SAUCE = 'SAUCE', 'Соусы и заправки'
        PRESERVES = 'PRESERVES', 'Заготовки'

    name = models.CharField(
        max_length=50,
        choices=CategoryChoices.choices,
        unique=True,
        default=CategoryChoices.SECOND_COURSE,
        verbose_name="Категория"
    )
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.get_name_display()

    def get_absolute_url(self):
        return reverse("cooking:category", kwargs={"slug": self.slug})


class Tag(models.Model):
    class TagChoices(models.TextChoices):
        QUICK = 'QUICK', 'Быстро'
        EASY = 'EASY', 'Просто'
        GOURMET = 'GOURMET', 'Празднично'
        VEGAN = 'VEGAN', 'Веганское'
        VEGETARIAN = 'VEGETARIAN', 'Вегетарианское'
        LENTEN = 'LENTEN', 'Постное'
        GLUTEN_FREE = 'GLUTEN_FREE', 'Без глютена'
        PP = 'PP', 'Правильное питание'
        KIDS = 'KIDS', 'Для детей'
        OVEN = 'OVEN', 'В духовке'
        MULTICOOKER = 'MULTICOOKER', 'В мультиварке'
        NO_BAKE = 'NO_BAKE', 'Без выпечки'
        GRILL = 'GRILL', 'На гриле'
        SPICY = 'SPICY', 'Острое'
        LOW_CAL = 'LOW_CAL', 'Низкокалорийное'
        PARTY = 'PARTY', 'Вечеринка'
        SOUP = 'SOUP', 'Суп'
        FAMILY = 'FAMILY', 'Семейное'
        BREAKFAST = 'BREAKFAST', 'Завтрак'
        HEARTY = 'HEARTY', 'Сытное'

    name = models.CharField(
        max_length=50,
        choices=TagChoices.choices,
        unique=True,
        default=TagChoices.EASY,
        verbose_name="Тег"
    )
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.get_name_display()

    def get_absolute_url(self):
        return reverse("cooking:tag", kwargs={"slug": self.slug})


class Cuisine(models.Model):
    class CuisineChoices(models.TextChoices):
        RUSSIAN = 'RUSSIAN', 'Русская'
        ITALIAN = 'ITALIAN', 'Итальянская'
        GEORGIAN = 'GEORGIAN', 'Грузинская'
        CHINESE = 'CHINESE', 'Китайская'
        JAPANESE = 'JAPANESE', 'Японская'
        FRENCH = 'FRENCH', 'Французская'
        UZBEK = 'UZBEK', 'Узбекская'
        EUROPEAN = 'EUROPEAN', 'Европейская'
        PAN_ASIAN = 'PAN_ASIAN', 'Пан-азиатская'
        OTHER = 'OTHER', 'Другая'

    name = models.CharField(
        max_length=10,
        choices=CuisineChoices.choices,
        default=CuisineChoices.OTHER,
        verbose_name="Кухня мира"
    )
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Кухня"
        verbose_name_plural = "Кухни"

    def __str__(self):
        return self.get_name_display()

    def get_absolute_url(self):
        return reverse("cooking:cuisine", kwargs={"slug": self.slug})



class Recipe(models.Model):
    author = models.ForeignKey(
        "Profile",
        on_delete=models.SET_NULL,
        null=True,
        related_name="recipes",
        verbose_name="Автор"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="recipes",
        verbose_name="Категория"
    )
    cuisine = models.ForeignKey(
        "Cuisine",
        on_delete=models.SET_NULL,
        null=True,
        related_name="recipes",
        verbose_name="Кухня"
    )
    tags = models.ManyToManyField(
        "Tag",
        related_name="recipes",
        verbose_name="Теги",
    )

    name = models.CharField(max_length=255, db_index=True, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание")
    instructions = models.TextField(verbose_name="Шаги приготовления")
    cooking_time = models.PositiveIntegerField(help_text="в минутах", verbose_name="Время приготовления")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cooking:recipe", kwargs={"slug": self.slug})


class Ingredient(models.Model):
    class UnitChoices(models.TextChoices):
        G = 'G', 'г'
        KG = 'KG', 'кг'
        ML = 'ML', 'мл'
        L = 'L', 'л'
        PC = 'PC', 'шт'
        TBSP = 'TBSP', 'ст. л.'
        TSP = 'TSP', 'ч. л.'
        CUP = 'CUP', 'стакан'
        PINCH = 'PINCH', 'щепотка'

    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=200, verbose_name="Название ингредиента")
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Количество",
        help_text="Например: 1.5 или 500"
    )
    unit = models.CharField(
        max_length=10,
        choices=UnitChoices.choices,
        default=UnitChoices.G,
        verbose_name="Единица измерения"
    )

    def __str__(self):
        amount_display = f"{self.amount:g}"
        return f"{self.name} — {amount_display} {self.get_unit_display()}"

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Профиль {self.user.username}"
