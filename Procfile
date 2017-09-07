web: gunicorn hackme.wsgi --log-file -
release: python manage.py flush --noinput && python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput