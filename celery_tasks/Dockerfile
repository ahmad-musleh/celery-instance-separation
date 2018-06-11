FROM python:3.6
LABEL maintainer="Ahmad Musleh {ahmad.s.musleh@gmail.com}"
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD celery -A tasks worker --loglevel=debug
