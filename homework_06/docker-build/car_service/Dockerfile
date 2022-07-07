FROM tiangolo/uwsgi-nginx-flask:python3.10

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY car_service_app /app
