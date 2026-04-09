from django import template
from django.db.models import QuerySet
from cooking.models import Category, Cuisine, Tag


register = template.Library()

@register.inclusion_tag("cooking/includes/sidebar.html")
def show_sidebar():
    categories: QuerySet[Category] = Category.objects.all()
    cuisines: QuerySet[Cuisine] = Cuisine.objects.all()
    tags: QuerySet[Tag] = Tag.objects.all()
    return {
        "categories": categories,
        "cuisines": cuisines,
        "tags": tags,
    }
