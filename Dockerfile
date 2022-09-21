FROM python:3.8.10
WORKDIR /app
ADD . /app
CMD ["python", "testing.py"]