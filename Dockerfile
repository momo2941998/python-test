FROM python:3.6.9

ENV HTTP_PROXY http://10.4.200.1:3000
ENV HTTPS_PROXY http://10.4.200.1:3000

# RUN apt add install python3-dev libpg-dev

# RUN pip install psycopg2

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./app /code/app
