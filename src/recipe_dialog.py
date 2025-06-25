from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QLineEdit, 
                            QComboBox, QTextEdit, QPushButton, QHBoxLayout,
                            QMessageBox)
from PyQt6.QtCore import Qt
from typing import Dict, Optional

class RecipeDialog(QDialog):
    def __init__(self, parent=None, recipe: Optional[Dict] = None, categories: list = None):
        super().__init__(parent)
        self.recipe = recipe
        self.categories = categories or []
        self.setup_ui()
        
        if recipe:
            self.populate_fields()
    
    def setup_ui(self):
        """Set up the dialog UI"""
        self.setWindowTitle("Add Recipe" if not self.recipe else "Edit Recipe")
        self.setModal(True)
        self.resize(500, 600)
        
        layout = QVBoxLayout(self)
        
        # Form layout for recipe fields
        form_layout = QFormLayout()
        
        # Recipe name
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Enter recipe name")
        form_layout.addRow("Recipe Name:", self.name_edit)
        
        # Category
        self.category_combo = QComboBox()
        self.category_combo.addItems(self.categories)
        self.category_combo.setEditable(True)
        form_layout.addRow("Category:", self.category_combo)
        
        # Ingredients
        self.ingredients_text = QTextEdit()
        self.ingredients_text.setPlaceholderText("List ingredients, one per line")
        self.ingredients_text.setMaximumHeight(150)
        form_layout.addRow("Ingredients:", self.ingredients_text)
        
        # Instructions
        self.instructions_text = QTextEdit()
        self.instructions_text.setPlaceholderText("Enter cooking instructions")
        form_layout.addRow("Instructions:", self.instructions_text)
        
        layout.addLayout(form_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")
        
        button_layout.addStretch()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)
        
        layout.addLayout(button_layout)
        
        # Connect signals
        self.save_button.clicked.connect(self.save_recipe)
        self.cancel_button.clicked.connect(self.reject)
        
        # Set default button
        self.save_button.setDefault(True)
    
    def populate_fields(self):
        """Populate fields with existing recipe data"""
        if not self.recipe:
            return
            
        self.name_edit.setText(self.recipe.get('name', ''))
        
        category = self.recipe.get('category', '')
        index = self.category_combo.findText(category)
        if index >= 0:
            self.category_combo.setCurrentIndex(index)
        else:
            self.category_combo.setCurrentText(category)
        
        self.ingredients_text.setPlainText(self.recipe.get('ingredients', ''))
        self.instructions_text.setPlainText(self.recipe.get('instructions', ''))
    
    def save_recipe(self):
        """Validate and save recipe data"""
        recipe_data = self.get_recipe_data()
        
        if not self.validate_recipe(recipe_data):
            return
        
        self.recipe_data = recipe_data
        self.accept()
    
    def get_recipe_data(self) -> Dict:
        """Get recipe data from form fields"""
        return {
            'name': self.name_edit.text().strip(),
            'category': self.category_combo.currentText().strip(),
            'ingredients': self.ingredients_text.toPlainText().strip(),
            'instructions': self.instructions_text.toPlainText().strip()
        }
    
    def validate_recipe(self, recipe_data: Dict) -> bool:
        """Validate recipe data and show error message if invalid"""
        if not recipe_data['name']:
            QMessageBox.warning(self, "Validation Error", "Recipe name is required.")
            self.name_edit.setFocus()
            return False
        
        if not recipe_data['category']:
            QMessageBox.warning(self, "Validation Error", "Category is required.")
            self.category_combo.setFocus()
            return False
        
        if not recipe_data['ingredients']:
            QMessageBox.warning(self, "Validation Error", "Ingredients are required.")
            self.ingredients_text.setFocus()
            return False
        
        if not recipe_data['instructions']:
            QMessageBox.warning(self, "Validation Error", "Instructions are required.")
            self.instructions_text.setFocus()
            return False
        
        return True