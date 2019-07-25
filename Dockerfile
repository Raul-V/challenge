FROM alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip && pip3 install psycopg2

WORKDIR /app

COPY ./app /app
COPY requirements.txt /app

RUN pip3 --no-cache-dir install -r requirements.txt                                                                            

EXPOSE 5000

ENTRYPOINT  ["python3"]

CMD ["app.py"]