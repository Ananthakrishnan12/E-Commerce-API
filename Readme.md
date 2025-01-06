# E-commerce API.

1.Install Required Libaries..
    -> pip install -r requirnments.txt

2.Create django project (Ecommerce).
   -> django-admin startproject Ecommerce
   -> cd Ecommerce
3.Create django application (shop).
   -> python manage.py startapp shop

4.Configure application with django in the settings.py
  'shop','rest_framework','rest_framework_simplejwt'

5.Configure the database configuration with Django in settings.py
6.create database table fields in the models.py for Registeration
7.specify the AUTH_USER_MODEL='shop.User' in the settings.py
8.Make the migrations in the database...
   -> python manage.py makemigrations
   -> python manage.py migrate
9.Configure the Ecommerce/urls.py.
10.create Endpoint for Register,Login,logout,userview in the views.py..
11.specify the endpoint urls in shop/urls.py
12.Before writing logic for endpoints specify serializer for User.. in shop/serializers.py
   Run the server...
13.API Testing with POSTMAN with urls
14.Install cors-headers to access frontend with API.
    -> 'corsheaders' in the settings.py
    -> 'corsheaders.middleware.CorsMiddleware'
    
        CORS_ORIGIN_ALLOW_ALL = True
        CORS_ALLOW_CREDENTIALS = True