from django.views import View

from shared.mixins.Response import JsonResponse
from shared.Generics import ListView, CreateView, RetrieveView

from .models import Category
from .forms import CategoryForm


class CategoryBase:
    def get_model(self):
        return Category

    def get_form(self, *args, **kwargs):
        return CategoryForm(*args, **kwargs)


class CategoryListView(View, CategoryBase, ListView, CreateView):
    def get_model(self):
        return Category

    def get_form(self, *args, **kwargs):
        return CategoryForm(*args, **kwargs)


class ClassDetailsView(View, CategoryBase, RetrieveView):
    def get_pk(self):
        return "id"
