from django.urls import path

from .views import CategoryListView, ClassDetailsView

urlpatterns = [
    path('', CategoryListView.as_view()),
    path('<int:pk>', ClassDetailsView.as_view())
]

