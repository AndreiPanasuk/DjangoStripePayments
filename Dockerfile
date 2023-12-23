FROM python:3.10

ENV PYTHONUNBUFFERED yes
ENV PYTHONDONTWRITEBYTECODE yes

ENV PIP_ROOT_USER_ACTION ignore
ENV PIP_NO_CACHE_DIR yes
ENV PIP_DISABLE_PIP_VERSION_CHECK yes

COPY requirements.txt /tmp/

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

COPY manage.py /manage.py
COPY db.sqlite3 /db.sqlite3
COPY ./.env /.env
COPY djstripe /djstripe
COPY spays /spays

WORKDIR /

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]