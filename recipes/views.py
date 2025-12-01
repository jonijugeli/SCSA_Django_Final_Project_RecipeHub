from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm

@login_required
def home_view(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes/home.html", {"recipes": recipes})

@login_required
def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect("recipes:home")
    else:
        form = RecipeForm()
    return render(request, "recipes/recipe_create.html", {"form": form})

@login_required
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.author != request.user:
        return redirect("recipes:home")
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipes:home")
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipes/recipe_update.html", {"form": form})

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.author != request.user:
        return redirect("recipes:home")
    if request.method == "POST":
        recipe.delete()
        return redirect("recipes:home")
    return render(request, "recipes/recipe_confirm_delete.html", {"recipe": recipe})
