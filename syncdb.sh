#！/bin/bash
source bio_database/bin/activate
cd bio_website/
python manage.py syncdb
python manage.py makemigrations
python manage.py migrate
