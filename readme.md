python3 -m virutalenv env
source env/bin/activate
pip3 install django
pip3 install psycopg2-binary
pip3 install djangorestframework
pip install django-cors-headers

// Edit setting to add module 'emp_details.apps.EmpDetailsConfig'


python manage.py makemigrations emp_details
python manage.py sqlmigrate emp_details XXXX
python manage.py migrate
python manage.py createsuperuser    //prajwal : admin@2020