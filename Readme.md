# intro
    
    A web base to do app ,used sqlite as backend .App has basic CRUD functions with interactive UI
    All main functionalities are implimented in todolist django app

# frontend 
    opensource html theme sneat

# packages

    django=4.2.13
    pytest =8.2.1
    python=3.9

# installation 

# create an enviroment using anaconda 
    conda create --name django_env python=3.9
    conda activate django_env
    
    pip install django
    pip install pytest
    
# get project 

    git clone https://github.com/MeharG811/to-do-app.git
    
# go to project root   

    cd to-do-app

# run Project

    python manage.py runserver 127.0.0.1:8001

# Run tests

    pytest

# run on unicorn server


python -m uvicorn to_do_app.asgi:application --port 9000

# build the docker image from docker file

docker build -t to_do_app:0.1 -f dockerfile.dockerfile .

# run docker image 

docker run -p 8023:8023 to_do_app:0.1