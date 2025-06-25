"""
Minecraft-themed stylesheet for the Recipe Planner application
Uses colors and styling inspired by Minecraft's blocky aesthetic
Qt-compatible version without unsupported CSS properties
"""

# Minecraft color palette
MINECRAFT_COLORS = {
    'grass_green': '#7CB342',
    'dirt_brown': '#8D6E63',
    'stone_gray': '#78909C',
    'cobblestone': '#546E7A',
    'wood_oak': '#D7CCC8',
    'wood_dark': '#8D6E63',
    'diamond_blue': '#42A5F5',
    'emerald_green': '#66BB6A',
    'gold_yellow': '#FFD54F',
    'redstone_red': '#EF5350',
    'lapis_blue': '#3F51B5',
    'coal_black': '#424242',
    'iron_silver': '#90A4AE',
    'water_blue': "#121313",
    'sky_blue': '#81C784',
    'orange': '#FF8F00',
    'purple': '#7E57C2',
    'pink': '#EC407A'
}

def get_minecraft_stylesheet():
    """
    Returns a complete stylesheet for the Recipe Planner with Minecraft theming
    Compatible with Qt/PyQt6
    """
    return f"""
    /* Main Window Styling */
    QMainWindow {{
        background-color: {MINECRAFT_COLORS['sky_blue']};
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 11pt;
    }}
    
    /* Central Widget */
    QWidget {{
        background-color: transparent;
        color: {MINECRAFT_COLORS['coal_black']};
    }}
    
    /* Group Boxes (Recipe List and Details panels) */
    QGroupBox {{
        font-weight: bold;
        font-size: 12pt;
        color: {MINECRAFT_COLORS['coal_black']};
        border: 3px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 8px;
        margin-top: 12px;
        padding-top: 8px;
        background-color: {MINECRAFT_COLORS['wood_oak']};
    }}
    
    QGroupBox::title {{
        subcontrol-origin: margin;
        left: 15px;
        padding: 0 8px 0 8px;
        color: {MINECRAFT_COLORS['coal_black']};
        background-color: {MINECRAFT_COLORS['gold_yellow']};
        border: 2px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 4px;
        font-weight: bold;
    }}
    
    /* Recipe List Widget */
    QListWidget {{
        background-color: {MINECRAFT_COLORS['stone_gray']};
        border: 2px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 6px;
        padding: 4px;
        selection-background-color: {MINECRAFT_COLORS['emerald_green']};
        selection-color: white;
        alternate-background-color: {MINECRAFT_COLORS['iron_silver']};
        font-size: 10pt;
    }}
    
    QListWidget::item {{
        background-color: {MINECRAFT_COLORS['wood_oak']};
        border: 1px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 4px;
        padding: 8px;
        margin: 2px;
        color: {MINECRAFT_COLORS['coal_black']};
    }}
    
    QListWidget::item:hover {{
        background-color: {MINECRAFT_COLORS['diamond_blue']};
        color: white;
        border-color: {MINECRAFT_COLORS['water_blue']};
    }}
    
    QListWidget::item:selected {{
        background-color: {MINECRAFT_COLORS['emerald_green']};
        color: white;
        border-color: {MINECRAFT_COLORS['grass_green']};
        font-weight: bold;
    }}
    
    /* Buttons */
    QPushButton {{
        background-color: {MINECRAFT_COLORS['grass_green']};
        border: 2px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 6px;
        padding: 8px 16px;
        font-weight: bold;
        color: white;
        min-height: 20px;
        font-size: 10pt;
    }}
    
    QPushButton:hover {{
        background-color: {MINECRAFT_COLORS['emerald_green']};
        border-color: {MINECRAFT_COLORS['grass_green']};
    }}
    
    QPushButton:pressed {{
        background-color: {MINECRAFT_COLORS['dirt_brown']};
        border-color: {MINECRAFT_COLORS['wood_dark']};
    }}
    
    QPushButton:disabled {{
        background-color: {MINECRAFT_COLORS['stone_gray']};
        color: {MINECRAFT_COLORS['iron_silver']};
        border-color: {MINECRAFT_COLORS['cobblestone']};
    }}
    
    /* Specific button colors */
    QPushButton[class="add"] {{
        background-color: {MINECRAFT_COLORS['emerald_green']};
    }}
    
    QPushButton[class="add"]:hover {{
        background-color: {MINECRAFT_COLORS['grass_green']};
    }}
    
    QPushButton[class="edit"] {{
        background-color: {MINECRAFT_COLORS['gold_yellow']};
        color: {MINECRAFT_COLORS['coal_black']};
    }}
    
    QPushButton[class="edit"]:hover {{
        background-color: {MINECRAFT_COLORS['orange']};
    }}
    
    QPushButton[class="delete"] {{
        background-color: {MINECRAFT_COLORS['redstone_red']};
    }}
    
    QPushButton[class="delete"]:hover {{
        background-color: #D32F2F;
    }}
    
    /* Text Inputs */
    QLineEdit {{
        background-color: white;
        border: 2px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 4px;
        padding: 6px;
        font-size: 10pt;
        selection-background-color: {MINECRAFT_COLORS['diamond_blue']};
    }}
    
    QLineEdit:focus {{
        border-color: {MINECRAFT_COLORS['diamond_blue']};
        background-color: {MINECRAFT_COLORS['water_blue']};
        color: white;
    }}
    
    /* Text Areas */
    QTextEdit {{
        background-color: white;
        border: 2px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 4px;
        padding: 6px;
        font-size: 10pt;
        selection-background-color: {MINECRAFT_COLORS['diamond_blue']};
    }}
    
    QTextEdit:focus {{
        border-color: {MINECRAFT_COLORS['emerald_green']};
    }}
    
    QTextEdit[readOnly="true"] {{
        background-color: {MINECRAFT_COLORS['wood_oak']};
        color: {MINECRAFT_COLORS['coal_black']};
    }}
    
    /* Combo Boxes */
    QComboBox {{
        background-color: {MINECRAFT_COLORS['wood_oak']};
        border: 2px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 4px;
        padding: 6px;
        font-size: 10pt;
        color: {MINECRAFT_COLORS['coal_black']};
        min-width: 100px;
    }}
    
    QComboBox:hover {{
        background-color: {MINECRAFT_COLORS['gold_yellow']};
    }}
    
    QComboBox::drop-down {{
        border: none;
        padding-right: 10px;
    }}
    
    QComboBox::down-arrow {{
        width: 0;
        height: 0;
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        border-top: 5px solid {MINECRAFT_COLORS['coal_black']};
        margin-right: 5px;
    }}
    
    QComboBox QAbstractItemView {{
        background-color: {MINECRAFT_COLORS['wood_oak']};
        border: 2px solid {MINECRAFT_COLORS['cobblestone']};
        selection-background-color: {MINECRAFT_COLORS['emerald_green']};
        selection-color: white;
    }}
    
    /* Labels */
    QLabel {{
        color: {MINECRAFT_COLORS['coal_black']};
        font-size: 10pt;
    }}
    
    QLabel[class="title"] {{
        font-size: 14pt;
        font-weight: bold;
        color: {MINECRAFT_COLORS['coal_black']};
        background-color: {MINECRAFT_COLORS['gold_yellow']};
        padding: 20px;
        border: 2px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 6px;
    }}

    QLabel[class="category"] {{
        font-size: 12pt;
        color: {MINECRAFT_COLORS['water_blue']};
        font-style: italic;
        text-align: center;
        margin-top: 5px;
        padding: 4px;
    }}
    
    /* Menu Bar */
    QMenuBar {{
        background-color: {MINECRAFT_COLORS['dirt_brown']};
        color: white;
        border-bottom: 2px solid {MINECRAFT_COLORS['cobblestone']};
        font-weight: bold;
        padding: 2px;
    }}
    
    QMenuBar::item {{
        background-color: transparent;
        padding: 6px 12px;
        border-radius: 4px;
    }}
    
    QMenuBar::item:selected {{
        background-color: {MINECRAFT_COLORS['grass_green']};
    }}
    
    QMenuBar::item:pressed {{
        background-color: {MINECRAFT_COLORS['emerald_green']};
    }}
    
    QMenu {{
        background-color: {MINECRAFT_COLORS['wood_oak']};
        border: 2px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 4px;
        padding: 4px;
    }}
    
    QMenu::item {{
        padding: 6px 20px;
        color: {MINECRAFT_COLORS['coal_black']};
        border-radius: 2px;
    }}
    
    QMenu::item:selected {{
        background-color: {MINECRAFT_COLORS['emerald_green']};
        color: white;
    }}
    
    /* Status Bar */
    QStatusBar {{
        background-color: {MINECRAFT_COLORS['stone_gray']};
        color: {MINECRAFT_COLORS['coal_black']};
        border-top: 2px solid {MINECRAFT_COLORS['cobblestone']};
        font-weight: bold;
        padding: 4px;
    }}
    
    /* Splitter */
    QSplitter::handle {{
        background-color: {MINECRAFT_COLORS['cobblestone']};
    }}
    
    QSplitter::handle:horizontal {{
        background-color: {MINECRAFT_COLORS['cobblestone']};
        width: 4px;
    }}
    
    QSplitter::handle:vertical {{
        background-color: {MINECRAFT_COLORS['cobblestone']};
        height: 4px;
    }}
    
    /* Dialog Styling */
    QDialog {{
        background-color: {MINECRAFT_COLORS['wood_oak']};
        border: 3px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 8px;
    }}
    
    /* Message Box Styling */
    QMessageBox {{
        background-color: {MINECRAFT_COLORS['wood_oak']};
        color: {MINECRAFT_COLORS['coal_black']};
    }}
    
    QMessageBox QPushButton {{
        min-width: 80px;
        margin: 2px;
    }}
    
    /* Scroll Bars */
    QScrollBar:vertical {{
        background-color: {MINECRAFT_COLORS['stone_gray']};
        width: 16px;
        border: 1px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 4px;
    }}
    
    QScrollBar::handle:vertical {{
        background-color: {MINECRAFT_COLORS['grass_green']};
        border: 1px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 4px;
        min-height: 20px;
    }}
    
    QScrollBar::handle:vertical:hover {{
        background-color: {MINECRAFT_COLORS['emerald_green']};
    }}
    
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
        background-color: {MINECRAFT_COLORS['dirt_brown']};
        height: 16px;
        border: 1px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 4px;
    }}
    
    QScrollBar:horizontal {{
        background-color: {MINECRAFT_COLORS['stone_gray']};
        height: 16px;
        border: 1px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 4px;
    }}
    
    QScrollBar::handle:horizontal {{
        background-color: {MINECRAFT_COLORS['grass_green']};
        border: 1px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 4px;
        min-width: 20px;
    }}
    
    QScrollBar::handle:horizontal:hover {{
        background-color: {MINECRAFT_COLORS['emerald_green']};
    }}
    
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
        background-color: {MINECRAFT_COLORS['dirt_brown']};
        width: 16px;
        border: 1px solid {MINECRAFT_COLORS['cobblestone']};
        border-radius: 4px;
    }}
    """


def apply_button_classes(main_window):
    """
    Apply specific CSS classes to buttons for individual styling
    """
    if hasattr(main_window, 'add_button'):
        main_window.add_button.setProperty("class", "add")
        main_window.add_button.style().polish(main_window.add_button)
    if hasattr(main_window, 'edit_button'):
        main_window.edit_button.setProperty("class", "edit")
        main_window.edit_button.style().polish(main_window.edit_button)
    if hasattr(main_window, 'delete_button'):
        main_window.delete_button.setProperty("class", "delete")
        main_window.delete_button.style().polish(main_window.delete_button)
    
    # Apply the class to title labels
    if hasattr(main_window, 'recipe_title'):
        main_window.recipe_title.setProperty("class", "title")
        main_window.recipe_title.style().polish(main_window.recipe_title)

    if hasattr(main_window, 'recipe_category'):
        main_window.recipe_category.setProperty("class", "category")
        main_window.recipe_category.style().polish(main_window.recipe_category)

def get_color_palette():
    """
    Returns the Minecraft color palette for use in other parts of the application
    """
    return MINECRAFT_COLORS