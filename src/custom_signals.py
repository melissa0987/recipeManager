from PyQt6.QtCore import QObject, pyqtSignal

class RecipeSignals(QObject):
    """Custom signals for recipe operations"""
    recipe_selected = pyqtSignal(dict)  # Emits recipe data when selected
    recipe_updated = pyqtSignal()       # Emits when recipe list needs refresh