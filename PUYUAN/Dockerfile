FROM python:3.10-alpine
RUN pip install django djangorestframework

WORKDIR /app
COPY . /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8787"]