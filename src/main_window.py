from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                            QListWidget, QTextEdit, QPushButton, QLineEdit,
                            QLabel, QMessageBox, QDialog,
                            QSplitter, QGroupBox, QListWidgetItem)
from PyQt6.QtCore import Qt 
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QAction, QKeySequence, QFont
from typing import Dict, Optional

# Fixed import - assuming styles.py is in the same directory as main_window.py
from .styles import get_minecraft_stylesheet, apply_button_classes

from .recipe_manager import RecipeManager
from .recipe_dialog import RecipeDialog
from .custom_signals import RecipeSignals

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.recipe_manager = RecipeManager()
        self.signals = RecipeSignals()
        self.current_recipe: Optional[Dict] = None
        
        self.setup_ui()
        self.create_menus()
        self.connect_signals()
        self.load_recipe_list()
        
        # Status bar message
        self.statusBar().showMessage("Ready")

        self.setStyleSheet(get_minecraft_stylesheet())
        apply_button_classes(self)
    
    def setup_ui(self):
        """Set up the main window UI"""
        self.setWindowTitle("Smart Recipe Planner")
        self.setGeometry(100, 100, 1000, 700)
        
        # Central widget with splitter
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        
        # Search bar
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Search:"))
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Search recipes...")
        search_layout.addWidget(self.search_edit)
        main_layout.addLayout(search_layout)

        # Category filter
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Filter by Category:"))
        self.category_filter = QComboBox()
        self.category_filter.setMinimumWidth(150)
        filter_layout.addWidget(self.category_filter)
        filter_layout.addStretch()
        main_layout.addLayout(filter_layout)
        
        # Main content splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left panel - Recipe list
        left_panel = QGroupBox("Recipes")
        left_layout = QVBoxLayout(left_panel)
        
        self.recipe_list = QListWidget()
        self.recipe_list.setMinimumWidth(300)
        left_layout.addWidget(self.recipe_list)
        
        # Buttons for recipe operations
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Recipe")
        self.edit_button = QPushButton("Edit")
        self.delete_button = QPushButton("Delete")
        
        self.edit_button.setEnabled(False)
        self.delete_button.setEnabled(False)
        
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addStretch()
        
        left_layout.addLayout(button_layout)
        splitter.addWidget(left_panel)
        
        # Right panel - Recipe preview
        right_panel = QGroupBox("Recipe Details")
        right_layout = QVBoxLayout(right_panel)
        
        self.recipe_title = QLabel("Select a recipe to view details")
        self.recipe_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.recipe_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.recipe_title.setStyleSheet("padding: 20px;")
        right_layout.addWidget(self.recipe_title)
        
        self.recipe_category = QLabel("") 
        right_layout.addWidget(self.recipe_category)
        
        # Ingredients
        right_layout.addWidget(QLabel("Ingredients:"))
        self.ingredients_display = QTextEdit()
        self.ingredients_display.setReadOnly(True)
        self.ingredients_display.setMaximumHeight(250)
        right_layout.addWidget(self.ingredients_display)
        
        # Instructions
        right_layout.addWidget(QLabel("Instructions:"))
        self.instructions_display = QTextEdit()
        self.instructions_display.setReadOnly(True)
        right_layout.addWidget(self.instructions_display)
        
        splitter.addWidget(right_panel)
        splitter.setSizes([400, 600])
        
        main_layout.addWidget(splitter)
    
    def create_menus(self):
        """Create menu bar and actions"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        
        new_action = QAction("New Recipe", self)
        new_action.setShortcut(QKeySequence.StandardKey.New)
        new_action.triggered.connect(self.add_recipe)
        file_menu.addAction(new_action)
        
        file_menu.addSeparator()
        
        save_action = QAction("Save", self)
        save_action.setShortcut(QKeySequence.StandardKey.Save)
        save_action.triggered.connect(self.save_recipes)
        file_menu.addAction(save_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.StandardKey.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu("Edit")
        
        add_recipe_action = QAction("Add Recipe", self)
        add_recipe_action.setShortcut(QKeySequence("Ctrl+A"))
        add_recipe_action.triggered.connect(self.add_recipe)
        edit_menu.addAction(add_recipe_action)
        
        delete_action = QAction("Delete Recipe", self)
        delete_action.setShortcut(QKeySequence.StandardKey.Delete)
        delete_action.triggered.connect(self.delete_recipe)
        edit_menu.addAction(delete_action)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        
        about_action = QAction("About", self)
        about_action.setShortcut(QKeySequence.StandardKey.HelpContents)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def connect_signals(self):
        """Connect all signals and slots"""
        self.add_button.clicked.connect(self.add_recipe)
        self.edit_button.clicked.connect(self.edit_recipe)
        self.delete_button.clicked.connect(self.delete_recipe)
        
        self.recipe_list.itemClicked.connect(self.on_recipe_selected)
        self.search_edit.textChanged.connect(self.filter_recipes)
        
        self.signals.recipe_selected.connect(self.display_recipe)
        self.signals.recipe_updated.connect(self.load_recipe_list)

        self.category_filter.currentTextChanged.connect(self.filter_by_category)
    
    def load_recipe_list(self):
        """Load recipes into the list widget"""
        self.load_category_filter()  # Refresh category filter
        self.filter_by_category()    # Apply current filters
    
    def filter_recipes(self):
        """Filter recipes based on search text and category"""
        self.filter_by_category()  # Use the combined filter method
   
    def load_category_filter(self):
        """Load categories into the filter dropdown"""
        self.category_filter.clear()
        self.category_filter.addItem("All Categories")
        
        # Get unique categories from existing recipes
        unique_categories = self.recipe_manager.get_unique_categories()
        self.category_filter.addItems(unique_categories)

    def filter_by_category(self):
        """Filter recipes by selected category"""
        selected_category = self.category_filter.currentText()
        search_term = self.search_edit.text().strip()
        
        # Get recipes by category
        if selected_category == "All Categories":
            recipes = self.recipe_manager.get_recipes()
        else:
            recipes = self.recipe_manager.get_recipes_by_category(selected_category)
        
        # Further filter by search term if provided
        if search_term:
            recipes = [r for r in recipes 
                    if search_term.lower() in r.get('name', '').lower() or 
                        search_term.lower() in r.get('ingredients', '').lower()]
        
        # Update the list
        self.recipe_list.clear()
        for recipe in recipes:
            item = QListWidgetItem(f"{recipe['name']} ({recipe['category']})")
            item.setData(Qt.ItemDataRole.UserRole, recipe)
            self.recipe_list.addItem(item)
        
        self.statusBar().showMessage(f"Found {len(recipes)} recipes")

    def on_recipe_selected(self, item: QListWidgetItem):
        """Handle recipe selection from list"""
        recipe = item.data(Qt.ItemDataRole.UserRole)
        self.current_recipe = recipe
        
        self.edit_button.setEnabled(True)
        self.delete_button.setEnabled(True)
        
        # Emit custom signal
        self.signals.recipe_selected.emit(recipe)
    
    def display_recipe(self, recipe: Dict):
        """Display selected recipe in the preview panel"""
        self.recipe_title.setText(recipe['name'])
        self.recipe_category.setText(f"Category: {recipe['category']}")
        self.ingredients_display.setPlainText(recipe['ingredients'])
        self.instructions_display.setPlainText(recipe['instructions'])
    
    def add_recipe(self):
        """Open dialog to add new recipe"""
        dialog = RecipeDialog(self, categories=self.recipe_manager.categories)
        
        if dialog.exec() == QDialog.DialogCode.Accepted:
            if self.recipe_manager.add_recipe(dialog.recipe_data):
                self.signals.recipe_updated.emit()
                self.statusBar().showMessage("Recipe added successfully")
            else:
                QMessageBox.critical(self, "Error", "Failed to add recipe")
    
    def edit_recipe(self):
        """Open dialog to edit selected recipe"""
        if not self.current_recipe:
            return
        
        dialog = RecipeDialog(self, recipe=self.current_recipe, 
                            categories=self.recipe_manager.categories)
        
        if dialog.exec() == QDialog.DialogCode.Accepted:
            recipe_id = self.current_recipe['id']
            if self.recipe_manager.update_recipe(recipe_id, dialog.recipe_data):
                self.signals.recipe_updated.emit()
                self.statusBar().showMessage("Recipe updated successfully")
            else:
                QMessageBox.critical(self, "Error", "Failed to update recipe")
    
    def delete_recipe(self):
        """Delete selected recipe"""
        if not self.current_recipe:
            return
        
        reply = QMessageBox.question(
            self, "Confirm Delete",
            f"Are you sure you want to delete '{self.current_recipe['name']}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            recipe_id = self.current_recipe['id']
            if self.recipe_manager.delete_recipe(recipe_id):
                self.signals.recipe_updated.emit()
                self.clear_recipe_display()
                self.statusBar().showMessage("Recipe deleted successfully")
            else:
                QMessageBox.critical(self, "Error", "Failed to delete recipe")
    
    def clear_recipe_display(self):
        """Clear the recipe preview panel"""
        self.recipe_title.setText("Select a recipe to view details")
        self.recipe_category.setText("")
        self.ingredients_display.clear()
        self.instructions_display.clear()
        
        self.current_recipe = None
        self.edit_button.setEnabled(False)
        self.delete_button.setEnabled(False)
    
    def save_recipes(self):
        """Save all recipes to file"""
        if self.recipe_manager.save_recipes():
            self.statusBar().showMessage("Recipes saved successfully")
        else:
            QMessageBox.critical(self, "Error", "Failed to save recipes")
    
    def show_about(self):
        """Show about dialog"""
        QMessageBox.about(
            self, "About Smart Recipe Planner",
            "Smart Recipe Planner v1.0\n\n"
            "A simple desktop application for managing recipes and meal planning.\n\n"
            "Built with Python and PyQt6"
        )