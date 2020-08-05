#!/bin/sh -e
echo "Applying migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput
echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Creating superuser account..."
python manage.py createsuperuser --noinput
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
exec "$@"
