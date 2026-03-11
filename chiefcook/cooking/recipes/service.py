from .recipes import recipes


class RecipesManager:
    def __init__(self, recipes_data: dict):
        self.recipes = recipes_data
        self.categories = {
            'breakfast': 'Завтраки',
            'lunch': 'Обеды',
            'dinner': 'Ужины'
        }

    def get_all_recipes(self) -> dict:
        return self.recipes

    def get_recipes_by_category(self, category: str) -> dict | None:
        return self.recipes.get(category)

    def get_recipe(self, category, recipe_id) -> dict | None:
        if category in self.recipes and recipe_id in self.recipes[category]:
            return self.recipes[category][recipe_id]
        return None

    def get_categories(self) -> dict:
        return self.categories

    def get_category_name(self, category: str) -> str | None:
        return self.categories.get(category)

    def get_recipes_count(self) -> int:
        total = 0
        for category in self.categories:
            total += len(self.recipes[category])
        return total

    def get_recipes_by_category_count(self, category: str) -> int | None:
        if category in self.recipes:
            return len(self.recipes[category])
        return None


recipes_manager = RecipesManager(recipes)
