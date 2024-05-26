intro
    
    A web base to do app ,used sqlite as backend .App has basic CRUD functions with interactive UI
    All main functionalities are implimented in todolist django app

frontend 
    opensource html theme sneat

packages

    django=4.2.13
    pytest =8.2.1
    python=3.9

installation 

->create an enviroment using anaconda 
    conda create --name django_env python=3.9
    conda activate django_env
    
    pip install django
    pip install pytest
    
run project 

    git clone https://github.com/MeharG811/to-do-app.git
    cd to-do-app
    python manage.py runserver 127.0.0.1:8001

Run tests

    cd to-do-app
    pytest
