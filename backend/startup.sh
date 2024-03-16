#!/bin/bash

python manage.py makemigrations
python manage.py migrate

# Create superuser non-interactively
python manage.py createsuperuser --noinput --username admin --email 12@gmail.com
python manage.py changepassword admin >>EOF
ILoveDjango
ILoveDjango
EOF

python manage.py runserver
