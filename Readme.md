# E-Commerce API

## Overview
The **E-Commerce API** is a backend application designed to handle the core functionalities of an online store. This project offers features like product management, order creation, and user authentication. It is an ideal starting point for developing scalable and secure e-commerce platforms.

---

## Features
- 🛍️ **Product Management**: Add, update, delete, and list products.
- 🛒 **Order Management**: Create and manage orders.
- 🔑 **Authentication**: Secure user authentication using JSON Web Tokens (JWT).
- 🛡️ **RESTful API**: Simple, clean, and RESTful API architecture.

---

## Technologies Used
- **Framework**: Django, Django REST Framework
- **Database**: MySQL
- **Programming Language**: Python
- **Authentication**: JSON Web Token (JWT)

---

## Prerequisites

1. **Create a Virtual Environment**:
   ```bash
   python -m venv (Project_name)
   cd (Project_name)
   activate

2. **Installation**:
   **clone the respository**
    ```bash
     git clone https://github.com/yourusername/Ecommerce-API.git
     cd Ecommerce-API

3. **Install Required Packages**
    ```bash
     pip install -r requirnments.txt

4. **Database Setup**
    ```bash
    In settings.py
         DATABASES ={
                'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '3306',
         }
    
5.**Migrations** 
    ```bash
    python manage.py makemigrations
    python manage.py migrate

6. **start the development server**
    ```bash
    python manage.py runserver


## API Testing DEMO...  ![API Testing Demo](https://github.com/Ananthakrishnan12/E-Commerce-API/blob/main/EcommerceAPI-Demo.gif)
                
