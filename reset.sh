#!/usr/bin/env bash

python manage.py flush --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py add-admin