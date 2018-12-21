# Bucketlist App

This app manages help user manage thier buckelist

# Features
	A user can be added[here](http://127.0.0.1:8000/)  
	Admin can add a new user and assign the user a password.[link](http://127.0.0.1:8000/admin)
	User can login using Username, Password,Email[link](http://127.0.0.1:8000/api/rest-auth/login/)
	A new item can be added.[link](http://127.0.0.1:8000/items/)
	A new item can be updated and deleted in the Bucketlist 

    

# Getting Started

    git clone this [repo](https://github.com/SelaDanti/Bucketlist.git)

   # Install requirements

   	pip3 install -r requirements.txt

    # Create Virtual Environment: 
    
    virtualenv env

    # Make Migrations :
    
    python3 manage.py makemigrations

    # Migrate:
    
    python3 manage.py migrate

    # Create tables that may not have existed:    
    
    python3 manage.py migrate --run-syncdb

    # create super user: 
    
    python manage.py createsuperuser


# Run project

	python3 manage.py runserver