FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential gcc

WORKDIR /app

RUN pip install uWSGI

COPY ./requirements.txt /app/
COPY ./hashtags_project /app/

RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "hashtags_project.wsgi:application"]
