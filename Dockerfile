FROM python:3.6-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev  

WORKDIR /app

COPY ./app /app
COPY requirements.txt /app

RUN pip3 --no-cache-dir install -r requirements.txt                                                                            

EXPOSE 5000

ENTRYPOINT  ["python3"]

CMD ["app.py"]