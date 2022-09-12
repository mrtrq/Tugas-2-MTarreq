release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json'
web: gunicorn katalogdisplay.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate