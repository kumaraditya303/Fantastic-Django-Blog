#!/bin/sh -e
python manage.py migrate --no-input --run-syncdb
python manage.py collectstatic --no-input
python manage.py createsuperuser --no-input
python manage.py runserver 0.0.0.0:8000
echo "$@"
