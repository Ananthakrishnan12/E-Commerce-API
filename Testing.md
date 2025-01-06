# API Testing..
Registration..
POST http://127.0.0.1:8000/api/register/

Excepted_input ={
    "name":"Ananthakrishnan",
    "email":"ananthmle@gmail.com",
    "password":"tensorflow97"
}

Excepted_output={
    "id": 1,
    "name": "Ananthakrishnan",
    "email": "ananthmle@gmail.com"
}

Login..
POST  http://127.0.0.1:8000/api/login/

Excepted_input={
    "email":"ramesh@gmail.com",
    "password":"ramesh97"
}

Excepted_output={
    "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiZXhwIjoxNzM2MDkxMDEyLCJpYXQiOjE3MzYwODc0MTJ9.QMkxRjLZG0nNrn7KPt1kvkyk5erAp0ZPReWPJpC1TUw"
}

# User Autheticated verify..
GET http://127.0.0.1:8000/api/user/

Excepted_output={
    "id": 3,
    "name": "ramesh",
    "email": "ramesh@gmail.com"
}

# Logout..
POST http://127.0.0.1:8000/api/logout/

Excepted_output={
    "message": "success"
}