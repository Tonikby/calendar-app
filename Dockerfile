FROM python:alpine

WORKDIR /app

COPY . .

VOLUME [ "/data" ]

CMD [ "python", "main.py" ]