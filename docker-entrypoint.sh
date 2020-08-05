#!/bin/sh -e
echo "Applying migrations..."
python manage.py migrate --noinput
echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Starting server..."
gunicorn djangoblog.wsgi
exec "$@"
