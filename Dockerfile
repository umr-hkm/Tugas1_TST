FROM python:3.8-slim-buster
WORKDIR /app
ADD . /app/
CMD [ "python", "tes.py" ]