FROM python:3.7
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD gunicorn wordchanger.wsgi:application --bind 0.0.0.0:8000