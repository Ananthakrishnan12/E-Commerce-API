# E-Commerce API 

Overview:
E-Commerce API is a backend application designed to handle core functionalities of an online store. This project provides features like product management, order creation, and user authentication. It's an excellent starting point for developing scalable and secure e-commerce platforms.

Features:
🛍️ Product management (add, update, delete, and list products).
🛒 Order creation and management.
🔑 Secure authentication and user management.
🛡️ Simple, clean, and RESTful API architecture.

Technologies Used:
       Framework: Django, Django REST Framework
       Database: MySQL
       Programming Language: Python
       Authentication: JSON Web Token (JWT)

prerequisites:
create a Virtual Environment:
    python -m venv (Project_name)
    cd (Project_name)
    activate

Installation:
Clone the repository:
    git clone https://github.com/yourusername/Ecommerce-API.git
    cd Ecommerce-API

Install Required Packages:
   pip install -r requirements.txt

Database Setup in Django Projects.. in settings.py
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Apply Migrations ..
      python manage.py makemigrations
      python manage.py migrate


Start the development Server:
      python manage.py runserver


