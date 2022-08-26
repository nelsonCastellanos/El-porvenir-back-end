FROM python:3.10.6-alpine3.16

ADD requirements.txt /app/requirements.txt

RUN set -ex \
    && apk add --no-cache --virtual .build-deps build-base \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && python -m pip install django \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

ADD . /app
WORKDIR /app

RUN python manage.py migrate 
RUN python manage.py collectstatic --noinput

ENV PATH /env/bin:$PATH

EXPOSE 8001



FROM nginx:1.22


CMD ["gunicorn", "--bind", ":8001", "--workers", "3", "el_porvenir.wsgi:application"]
