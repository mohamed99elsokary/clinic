FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /

COPY ./requirements/base.txt /requirements/base.txt
COPY ./requirements/local.txt /requirements/local.txt
RUN pip install --cache-dir=/root/.pip -r ./requirements/local.txt

COPY ./compose/production/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/start.sh /
RUN sed -i 's/\r$//g' /start.sh

WORKDIR /code
COPY . /code/

ENTRYPOINT ["/entrypoint"]
