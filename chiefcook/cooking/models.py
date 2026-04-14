from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from unidecode import unidecode

from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Категория"
    )
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(unidecode(self.name))
            return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("cooking:category", kwargs={"slug": self.slug})


class Cuisine(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Название кухни"
    )
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = "Кухня"
        verbose_name_plural = "Кухни"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(unidecode(self.name))
            return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("cooking:cuisine", kwargs={"slug": self.slug})


class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Название тега"
    )
    slug = models.SlugField(max_length=50, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(unidecode(self.name))
            return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("cooking:tag", kwargs={"slug": self.slug})


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
    tags = models.ManyToManyField("Tag", related_name="recipes")

    name = models.CharField(max_length=255, db_index=True, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание")
    instructions = models.TextField(verbose_name="Шаги приготовления")
    cooking_time = models.PositiveIntegerField(help_text="в минутах", verbose_name="Время приготовления")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(unidecode(self.name))
            return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("cooking:recipe", kwargs={"slug": self.slug})


class Ingredient(models.Model):
    class UnitChoices(models.TextChoices):
        G = 'G', 'г.'
        KG = 'KG', 'кг.'
        ML = 'ML', 'мл.'
        L = 'L', 'л.'
        PC = 'PC', 'шт.'
        TBSP = 'TBSP', 'ст. л.'
        TSP = 'TSP', 'ч. л.'
        CUP = 'CUP', 'стакан'
        PINCH = 'PINCH', 'щепотка'

    recipe = models.ForeignKey(
        "Recipe",
        on_delete=models.CASCADE,
        related_name='ingredients',
        verbose_name="Ингредиент"
    )
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
        return self.name

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
