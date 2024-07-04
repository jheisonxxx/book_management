#!/bin/sh
echo "Running Application"
python manage.py collectstatic --no-input
gunicorn book_management.wsgi:application --bind 0.0.0.0:8000