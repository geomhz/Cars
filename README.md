# Car Management System

## About the Project

This project is a simple car registration system developed with the Django framework. It is designed to facilitate the organization of car registration, offering various useful functionalities for efficient management.

### Funcionalidades

- **Login Screen:** Secure authentication to access the system.
- **Registration Screen:** User registration to access the system.
- **Car search filter:** The filter makes it easier to search for a car by name/brand.
- **Create/Read/Update/Delete (CRUD) cars:** For logged-in users, it is possible to add a new registration, see a list of registered cars, update the registration of an existing car, or delete an existing car.
- **Administrator (DJANGO-ADMIN):** Control and administration of all accesses present on the platform.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Install the following prerequisites to run the project:

- Python 3.8+ installed on the machine.

### Installation

Follow the steps below to set up the development environment:

1. Clone the repository
```bash
git clone https://github.com/geomhz/car-store-django.git

```

1. Create a virtual environment and activate it
```bash
Windows: python -m venv venv
         venv/scripts/activate

Linux/Mac: python3 -m venv venv
           source venv/bin/activate
```

3. Install the dependencies
```bash
pip install -r requirements.txt
```
4. Execute the migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the server
```bash
python manage.py runserver
```

### Dependencies

Lista de dependências do projeto:
```bash
asgiref==3.7.2
Django==5.0.2
pillow==10.2.0
sqlparse==0.4.4
tzdata==2024.1
```

## Usage

You can create a superuser to get acess on /admin/ or just skip this step (you can register as normal user):
```bash
python manage.py createsuperuser
```

To start the system with the command:
```bash
python manage.py runserver
```

Open a browser and navigate locally:
```bash
http://127.0.0.1:8000/
```

View the list of available cars without having access to edits:
NOTE: By clicking on any car image from the available list, you will have access to the car's details.
```bash
http://127.0.0.1:8000/cars/
```

Sign-up in the system to gain access to CRUD (CREATE, READ, UPDATE, and DELETE):
```bash
http://127.0.0.1:8000/register/
```

Log in to access the system:
```bash
http://127.0.0.1:8000/login/
```

After logging in with the new account created, you will have access to car edits by clicking on the image of any car.
```bash
http://127.0.0.1:8000/cars/
```

Register a new car. The upload images will be automatically added to the "media" folder located at the root of the project!
```bash
http://127.0.0.1:8000/new_car/
```

There you go! Now that you know how to navigate the system, you can start exploring!!

## Contact
My name is Geovanne Murata!

Website - [Visit my website!](https://geomurata.com/)

Linked In - [Visit my LinkedIn!](https://www.linkedin.com/in/geovanne-murata/)

WhatsApp - [Text me on WhatsApp!](https://api.whatsapp.com/send/?phone=5511952842140)

Project Link: [car-store-django](https://github.com/geomhz/car-store-django/)