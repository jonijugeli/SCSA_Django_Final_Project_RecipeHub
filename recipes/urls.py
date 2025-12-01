from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path('', views.home_view, name="home"),
    path('create/', views.recipe_create, name="recipe_create"),
    path('update/<int:pk>/', views.recipe_update, name="recipe_update"),
    path('delete/<int:pk>/', views.recipe_delete, name="recipe_delete"),
]
