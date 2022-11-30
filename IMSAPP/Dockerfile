FROM python:3.8.5-slim-buster

RUN mkdir /project

COPY . /project

WORKDIR /project

COPY ./requirements.txt /project

RUN pip install -r requirements.txt

ENV FLASK_ENV 0

ENV FLASK_APP=./project/__init__.py

ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 4000

# Run Flask command
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "4000"]
