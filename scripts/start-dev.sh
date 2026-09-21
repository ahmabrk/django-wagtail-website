#!/usr/bin/env sh
set -e

python manage.py makemigrations home blog books --noinput || true
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear || true
python manage.py runserver 0.0.0.0:8000
