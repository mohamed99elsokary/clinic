FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /

COPY ./requirements/base.txt /requirements/base.txt
COPY ./requirements/production.txt /requirements/production.txt
COPY ./requirements.txt /requirements.txt
RUN pip install --cache-dir=/root/.pip -r ./requirements.txt

COPY ./compose/production/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/production/start.sh /

WORKDIR /code
COPY . /code/

ENTRYPOINT ["/entrypoint"]
