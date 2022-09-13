release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json'
web: gunicorn project_django.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate

# nama .wsgi harus sama dengan nama folder lokasi wsgi.py tersimpan
# saya mengalami app crash karena hal tersebut
# sekarang sudah solved