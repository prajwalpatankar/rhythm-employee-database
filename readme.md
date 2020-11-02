## setting up frontend
cd client  
npm install  
  

## run frontend server
ng serve  


## setting up server
cd ..  
cd server  
python3 -m virutalenv env  
source env/bin/activate  
pip3 install django  
pip3 install psycopg2-binary  
pip3 install djangorestframework  
pip install django-cors-headers  
  
  
## run backend server
python manage.py runserver  
  
  
## Commands for migrations
python manage.py makemigrations emp_details  
python manage.py sqlmigrate emp_details XXXX  
python manage.py migrate  
python manage.py createsuperuser    //prajwal : rhythm123  