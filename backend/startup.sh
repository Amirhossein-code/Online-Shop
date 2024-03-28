#!/bin/bash

echo "Creating migrations"
python manage.py makemigrations

echo "migrating database"
python manage.py migrate

echo "Creating SUperUser"
python manage.py createsuperuser --email admin12@gmail.com --username admin

# python manage.py seed

echo "Running development server"
python manage.py runserver
