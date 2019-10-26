FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get -y upgrade

COPY ./website/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./compose/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY ./compose/django/startprod /startprod
RUN sed -i 's/\r//' /startprod
RUN chmod +x /startprod

COPY ./compose/django/start-celerybeat /start-celerybeat
RUN sed -i 's/\r//' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/django/start-celeryworker /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/django/start-flower /start-flower
RUN sed -i 's/\r//' /start-flower
RUN chmod +x /start-flower

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
