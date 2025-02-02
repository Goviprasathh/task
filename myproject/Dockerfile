
FROM python:3.11.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /bharat_app


WORKDIR /bharat_app


COPY . /bharat_app


RUN pip install -r requirements.txt


EXPOSE 8000


ENV NAME World


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
