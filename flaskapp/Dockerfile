FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
ADD wsgi.ini wsgi.ini
RUN pip install -r requirements.txt
COPY app.py app.py
CMD ["uwsgi", "wsgi.ini"]
