release: python3 manage.py migrate
web: python manage.py collectstatic --noinput; gunicorn django_shop.wsgi —-log-file -
