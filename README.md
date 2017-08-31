Add 127.0.0.1 db to your /etc/hosts if you plan to run migrations or manage.py commands

superuser is admin, admin@example.com, tweddle646

To run application for the first time

```
%docker-compose up -d
%python manage.py makemigrations
%python manage.py migrate
```

To restart after configuration changes are made

```
%docker-compose restart
```