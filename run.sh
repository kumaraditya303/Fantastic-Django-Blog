#!/bin/sh -e

echo "Setting up environment variables..."
export $(grep -v '^#' .env | xargs )
echo "Applying migrations..."
python manage.py makemigrations --noinput || python3 manage.py makemigrations --noinput || python3.8 manage.py makemigrations --noinput
python manage.py migrate --noinput || python3 manage.py migrate --noinput || python3.8 manage.py migrate --noinput
echo "Collecting static files..."
python manage.py collectstatic --noinput || python3 manage.py collectstatic --noinput || python3.8 manage.py collectstatic --noinput
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000 || python3 manage.py runserver 0.0.0.0:8000 || python3.8 manage.py runserver 0.0.0.0:8000
exec "$@"
