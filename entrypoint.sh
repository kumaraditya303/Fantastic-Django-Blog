#!/bin/sh

if [ "$SQL_DATABASE" = "data" ]
then
    echo "PostgreSQL started"
    echo "Applying migrations to database"
    python manage.py migrate --no-input
    echo "Finished database migrations "
fi

echo "Collecting static files..."
python manage.py collectstatic --no-input
echo "Finished collecting static files!"
echo "Starting server..."
gunicorn --bind 0.0.0.0:8000 djangoblog.wsgi 
echo "$@"
