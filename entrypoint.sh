#!/bin/sh
echo "Running Application"
gunicorn src.wsgi:application --bind 0.0.0.0:8000