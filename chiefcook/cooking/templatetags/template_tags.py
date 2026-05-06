from django import template
from urllib.parse import urlencode
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


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context["request"].GET.copy()

    for key, value in kwargs.items():
        if value == "" or value is None:
            query.pop(key, None)
        else:
            query[key] = value
    encoded = urlencode(query)
    if encoded:
        return "?" + encoded
    return ""