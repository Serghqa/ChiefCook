from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, Page

from .models import Recipe


class RecipeQuerysetMixin:
    paginate_by = 9

    def get_queryset(self):
        return Recipe.objects.select_related("author__user", "category", "cuisine")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "paginator" in context and "page_obj" in context:
            paginator: Paginator = context["paginator"]
            page_obj: Page = context["page_obj"]
            context["page_range"] = paginator.get_elided_page_range(
                page_obj.number,
                on_each_side=1,
                on_ends=2
            )
        return context


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
