import json
import os
from typing import List, Dict, Optional

class RecipeManager:
    def __init__(self, data_file: str = "data/recipes.json"):
        self.data_file = data_file
        self.recipes: List[Dict] = []
        self.categories = ["Breakfast", "Lunch", "Dessert", "Dinner", "Snack", "Vegetarian", "Vegan"]
        self.load_recipes()
    
    def load_recipes(self) -> bool:
        """Load recipes from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.recipes = json.load(f)
            return True
        except Exception as e:
            print(f"Error loading recipes: {e}")
            return False

    def get_recipes_by_category(self, category: str) -> List[Dict]:
        """Get recipes filtered by category, sorted alphabetically"""
        if category == "All Categories":
            recipes = self.recipes
        else:
            recipes = [r for r in self.recipes if r.get('category', '').lower() == category.lower()]
        
        # Always return sorted results
        return sorted(recipes, key=lambda recipe: recipe.get('name', '').lower())

    def get_recipes_sorted_alphabetically(self) -> List[Dict]:
        """Get all recipes sorted alphabetically by name"""
        return sorted(self.recipes, key=lambda recipe: recipe.get('name', '').lower())

    def get_unique_categories(self) -> List[str]:
        """Get all unique categories from existing recipes"""
        categories = set(recipe.get('category', '') for recipe in self.recipes)
        categories = [cat for cat in categories if cat.strip()]  # Remove empty categories
        return sorted(categories)
    
    def save_recipes(self) -> bool:
        """Save recipes to JSON file"""
        try:
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.recipes, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving recipes: {e}")
            return False
    
    def add_recipe(self, recipe: Dict) -> bool:
        """Add a new recipe"""
        if self.validate_recipe(recipe):
            recipe['id'] = len(self.recipes) + 1
            self.recipes.append(recipe)
            return self.save_recipes()
        return False
    
    def update_recipe(self, recipe_id: int, updated_recipe: Dict) -> bool:
        """Update an existing recipe"""
        if self.validate_recipe(updated_recipe):
            for i, recipe in enumerate(self.recipes):
                if recipe.get('id') == recipe_id:
                    updated_recipe['id'] = recipe_id
                    self.recipes[i] = updated_recipe
                    return self.save_recipes()
        return False
    
    def delete_recipe(self, recipe_id: int) -> bool:
        """Delete a recipe by ID"""
        self.recipes = [r for r in self.recipes if r.get('id') != recipe_id]
        return self.save_recipes()
    
    def get_recipes(self) -> List[Dict]:
        """Get all recipes sorted alphabetically"""
        return self.get_recipes_sorted_alphabetically()
    
    def search_recipes(self, query: str) -> List[Dict]:
        """Search recipes by name or ingredients, sorted alphabetically"""
        query = query.lower()
        matching_recipes = [r for r in self.recipes 
                           if query in r.get('name', '').lower() or 
                              query in r.get('ingredients', '').lower()]
        return sorted(matching_recipes, key=lambda recipe: recipe.get('name', '').lower())
    
    def validate_recipe(self, recipe: Dict) -> bool:
        """Validate recipe data"""
        required_fields = ['name', 'category', 'ingredients', 'instructions']
        return all(recipe.get(field, '').strip() for field in required_fields)