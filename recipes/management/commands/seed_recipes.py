from django.core.management.base import BaseCommand
from recipes.models import Recipe
from users.models import CustomUser
from django.utils.crypto import get_random_string
import random

class Command(BaseCommand):
    help = "Creates 10 random Recipe objects with an author"

    def handle(self, *args, **kwargs):
        try:
            author = CustomUser.objects.first()
            if not author:
                self.stdout.write(self.style.ERROR("No users found! Please create a user first."))
                return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error fetching user: {e}"))
            return

        for _ in range(10):
            title = "Recipe " + get_random_string(5)
            description = "Random generated recipe " + get_random_string(20)
            cooking_time = random.randint(5, 120)

            Recipe.objects.create(
                title=title,
                description=description,
                author=author,
                cooking_time=cooking_time
            )

        self.stdout.write(self.style.SUCCESS("Successfully added 10 random recipes!"))
