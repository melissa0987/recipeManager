# Recipe Manager

A comprehensive recipe management application for storing recipes with ingredients, instructions, and meal planning capabilities.

> **Educational Project**: This application was created for educational purposes as part of a programming course. It serves as a learning exercise to demonstrate software development concepts including database management, user interface design, and application architecture.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
  - [Managing Recipes](#managing-recipes)
  - [Ingredients Management](#ingredients-management)
  - [Meal Planning](#meal-planning)
- [API Reference](#api-reference) 
- [License](#license)
- [Support](#support)

## Overview

Recipe Manager is a user-friendly application designed to help you organize, store, and plan your culinary adventures. Whether you're a home cook or a professional chef, this tool provides an efficient way to manage your recipe collection and plan meals.

## Features

### Core Functionality
- **Recipe Storage**: Store unlimited recipes with detailed information
- **Ingredient Management**: Track ingredients with quantities and units
- **Step-by-Step Instructions**: Clear, organized cooking instructions
- **Meal Planning**: Plan meals for days, weeks, or months ahead
- **Search & Filter**: Quickly find recipes by name, ingredient, or category
- **Categories & Tags**: Organize recipes with custom categories and tags

### Additional Features
- **Nutritional Information**: Track calories and nutritional data
- **Cooking Time Tracking**: Prep time, cook time, and total time
- **Serving Size Management**: Scale recipes up or down
- **Shopping Lists**: Generate shopping lists from planned meals
- **Recipe Import/Export**: Import from popular formats or websites
- **Photo Support**: Add images to your recipes
- **Rating System**: Rate and review your recipes
- **Notes & Modifications**: Track recipe variations and personal notes

## Installation

### Prerequisites
- [List specific requirements based on technology stack]
- [e.g., Python 3.8+, Node.js 14+, etc.]

### Quick Start
```bash
# Clone the repository
git clone https://github.com/melissa0987/recipeManager.git

# Navigate to the project directory
cd recipeManager

# Install dependencies
pip install PyQt6

# Run the application
python main.py
```

### Alternative Installation Methods
- Docker installation (if applicable)
- Package manager installation
- Pre-built binaries

## Getting Started

### First Run
1. Launch the application
2. Create your first recipe collection
3. Add your favorite recipe
4. Explore the meal planning features

### Basic Workflow
1. **Add Recipes**: Input your recipes with ingredients and instructions
2. **Organize**: Use categories and tags to organize your collection
3. **Plan Meals**: Create meal plans for the week or month
4. **Generate Lists**: Create shopping lists from your meal plans
5. **Cook & Enjoy**: Follow your organized recipes and meal plans

## Usage

### Managing Recipes

#### Adding a New Recipe
```
1. Click "Add Recipe" or use the + button
2. Fill in recipe details:
   - Recipe name
   - Description
   - Category/tags
   - Prep time and cook time
   - Serving size
3. Add ingredients with quantities
4. Enter step-by-step instructions
5. Upload photos (optional)
6. Save the recipe
```

#### Editing Recipes
- Select a recipe from your collection
- Click "Edit" to modify any details
- Save changes when complete

#### Recipe Categories
- Create custom categories (e.g., "Breakfast", "Desserts", "Vegetarian")
- Assign multiple categories to recipes
- Filter recipes by category

### Ingredients Management

#### Adding Ingredients
- Add ingredients individually or from a master list
- Specify quantities with appropriate units
- Set ingredient categories for better organization

#### Unit Conversions
- Automatic conversion between units (cups to milliliters, etc.)
- Support for metric and imperial measurements
- Custom unit definitions

#### Inventory Tracking
- Track available ingredients
- Get alerts for low stock items
- Integration with shopping lists

### Meal Planning

#### Creating Meal Plans
1. Navigate to the Meal Planning section
2. Select the time period (week, month, etc.)
3. Drag and drop recipes onto specific days
4. Balance meals across different categories
5. Review nutritional information

#### Meal Plan Features
- **Calendar View**: Visual representation of planned meals
- **Nutritional Overview**: Track calories and nutrients across meals
- **Shopping List Generation**: Automatically create shopping lists
- **Recipe Scaling**: Adjust serving sizes based on planned portions

#### Shopping Lists
- Generate lists from meal plans
- Organize by store sections
- Check off items as you shop
- Share lists with family members

## API Reference

### Recipe Operations
```
GET /api/recipes          - Get all recipes
GET /api/recipes/{id}     - Get specific recipe
POST /api/recipes         - Create new recipe
PUT /api/recipes/{id}     - Update recipe
DELETE /api/recipes/{id}  - Delete recipe
```

### Ingredient Operations
```
GET /api/ingredients      - Get all ingredients
POST /api/ingredients     - Add new ingredient
PUT /api/ingredients/{id} - Update ingredient
DELETE /api/ingredients/{id} - Delete ingredient
```

### Meal Plan Operations
```
GET /api/mealplans        - Get meal plans
POST /api/mealplans       - Create meal plan
PUT /api/mealplans/{id}   - Update meal plan
DELETE /api/mealplans/{id} - Delete meal plan
```
 

### Customization Options
- Theme selection (light/dark mode)
- Default measurement units
- Recipe template customization
- Category and tag management
- Backup and sync preferences

## Data Management

### Backup and Restore
- Automatic daily backups
- Manual backup creation
- One-click restore functionality
- Export data in multiple formats

### Import Options
- Import from popular recipe formats
- Web scraping from recipe websites
- Bulk import from CSV/Excel files
- Integration with other recipe apps

### Export Options
- PDF recipe cards
- Printable meal plans
- Shopping list exports
- Data backup files

## Troubleshooting

### Common Issues
1. **Recipes not saving**
   - Check database permissions
   - Verify disk space availability
   - Ensure all required fields are filled

2. **Import failures**
   - Verify file format compatibility
   - Check for special characters in recipe names
   - Ensure proper encoding (UTF-8)

3. **Performance issues**
   - Clear application cache
   - Optimize database (if applicable)
   - Check system requirements

### Error Messages
- **"Database connection failed"**: Check database configuration
- **"Recipe validation error"**: Ensure all required fields are completed
- **"Import format not supported"**: Use supported file formats


## License

This project is licensed under the MIT License - see the LICENSE file for details.

### MIT License

```
MIT License

Copyright (c) 2024 Melissa Louise Bangloy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Support

### Getting Help
- **Documentation**: Check this README and wiki pages
- **Issues**: Report bugs and request features on GitHub
- **Community**: Join discussions in the repository

### Contact Information
- **Repository**: https://github.com/melissa0987/recipeManager
- **Issues**: https://github.com/melissa0987/recipeManager/issues

## Changelog

### Version History
- **v1.0.0** - Initial release with core features
- **v1.1.0** - Added meal planning functionality
- **v1.2.0** - Enhanced ingredient management
- **Current** - Latest improvements and bug fixes

## Acknowledgments

- Contributors and community members
- Third-party libraries and tools used
- Recipe data sources and inspiration
- Course instructors and educational institution for project guidance

## Educational Context

This Recipe Manager application was developed as part of a programming course project. The goals of this educational project include:

- **Learning Software Architecture**: Understanding how to structure a full-stack application
- **Database Design**: Implementing proper data relationships and storage patterns
- **User Interface Development**: Creating intuitive and responsive user interfaces
- **API Development**: Building RESTful APIs for data management
- **Testing Practices**: Implementing unit tests and integration tests
- **Documentation**: Creating comprehensive project documentation
- **Version Control**: Using Git and GitHub for collaborative development

### Learning Outcomes
Students working on this project will gain experience in:
- Full-stack web development
- Database design and management
- RESTful API development
- User experience (UX) design principles
- Software testing methodologies
- Project documentation and maintenance

### Course Integration
This project can be adapted for various programming courses including:
- Web Development Fundamentals
- Database Systems
- Software Engineering
- Human-Computer Interaction
- Project Management in Software Development

---

*Last updated: [Current Date]*
*For the most current information, please visit the [GitHub repository](https://github.com/melissa0987/recipeManager)*