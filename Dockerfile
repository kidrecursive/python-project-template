FROM python:3.7-alpine

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app

ENV FLASK_APP=app/web.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001", "--with-threads"]
