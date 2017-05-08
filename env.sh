#！/bin/bash
source bio_database/bin/activate
cd bio_website/
python manage.py syncdb
