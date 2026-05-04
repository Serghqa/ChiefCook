from django.shortcuts import get_object_or_404

from .models import Recipe


class RecipeQuerysetMixin:
    def get_queryset(self):
        return Recipe.objects.select_related("author__user", "category", "cuisine")


class FilteredQuerysetMixin(RecipeQuerysetMixin):
    filter_model = None
    filter_field = None
    context_name = None

    def get_queryset(self):
        slug = self.kwargs["slug"]
        self.filter_obj = get_object_or_404(self.filter_model, slug=slug)
        return super().get_queryset().filter(**{self.filter_field: self.filter_obj})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_name] = self.filter_obj
        return context
