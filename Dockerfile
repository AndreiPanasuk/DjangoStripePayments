FROM python:3.10

ENV PYTHONUNBUFFERED yes
ENV PYTHONDONTWRITEBYTECODE yes

ENV PIP_ROOT_USER_ACTION ignore
ENV PIP_NO_CACHE_DIR yes
ENV PIP_DISABLE_PIP_VERSION_CHECK yes

ENV DJANGO_SECRET_KEY django-insecure-%l6tp9rvv8*1*5r76u&u4rsl)-*66xzx3l64f2v2sl3c7yx4+6
ENV STRIPE_PUBLISHABLE_KEY pk_test_51OQ5MDLH4UwvJ9hjJzPKvNhK9WIyqEL4lCiV6Kf0rHvgaXARSKiZMzqAmUDCPtvUgtjmmgcjFA4KMLOV9luUPrPU00F7QA4ehi
ENV STRIPE_SECRET_KEY sk_test_51OQ5MDLH4UwvJ9hj9OKiZ0Vx9h7L0bfRtBaXRrFlIKAQvTFDWipnF1Ona44qC1FoDreC91U7xb5S5790gYe6NBnD009kBT4H4q

COPY requirements.txt /tmp/

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

COPY manage.py /manage.py
COPY db.sqlite3 /db.sqlite3
COPY .env /.env
COPY djstripe /djstripe
COPY spays /spays

WORKDIR /

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]