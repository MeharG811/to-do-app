from python:3.9-bullseye

ADD . /to_do_app

WORKDIR /to_do_app

Run pip install --no-cache-dir  -r requirements.txt

EXPOSE 8023

CMD ["python", "manage.py", "runserver", "0.0.0.0:8023"] 
