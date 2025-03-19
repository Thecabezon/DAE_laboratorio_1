# 🚀 Lab 1 - Django Project

A web project developed with Django, following a clean and organized structure.

## 📋 Overview

This project follows a custom structure:
- `src/`: Main code directory
  - `config/`: Project configuration
  - `core/`: Main application
- `venv/`: Virtual environment (not tracked in Git)

## ✨ Features

- 📱 Clean and organized structure with Django
- 🛠️ Separation of configuration and application code
- 📦 Ready to integrate with frontend frameworks
- 🔒 Admin interface for content management

## 🔧 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/DAE_laboratorio_1.git
   cd DAE_laboratorio_1/laboratorio_1

2. Create and activate a virtual environment:
  On Linux/MacOS: python3 -m venv venv
                  source venv/bin/activate
  On Windows: python -m venv venv
              venv\Scripts\activate
3. Install dependencies: pip install -r requirements.txt
4. Apply migrations: python manage.py migrate
5. Create a superuser: python manage.py createsuperuser

🚀 Running the project
- Start the development server: python manage.py runserver
- Access the site at:
    Main site: http://127.0.0.1:8000/
    Admin panel: http://127.0.0.1:8000/admin/
🛠️ Development
- Add models in core/models.py
- Create views in core/views.py
- Add URL patterns in core/urls.py
- Create templates in core/templates/

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

👤 Author
Jefferson Rojas Sosa

Built with ❤️ using Django.
