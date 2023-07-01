FROM ubuntu:focal-20230605
# because ubuntu-focal uses python3 for latest python3.9 and pip3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ubuntu does not have /code by default
RUN mkdir /code
WORKDIR /code
# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip3 install pip-tools
RUN pip-sync /requirements/base.txt /requirements/production.txt

COPY . /code/


# copy out /start-web_django
# start-web_django executes `migrate` and `runserver 0.0.0.0:8000`
COPY ./docker/local/django/start-web_django /start-web_django
RUN sed -i 's/\r//' /start-web_django
RUN chmod +x /start-web_django