#!/bin/bash

echo "Creating migrations"
python manage.py makemigrations

echo "Creating Store migrations"
python manage.py makemigrations store

echo "Creating Core migrations"
python manage.py makemigrations core

echo "migrating database"
python manage.py migrate

echo "Running development server"
python manage.py runserver