FROM public.ecr.aws/bitnami/python:3.9.5
# FROM python:3.8

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

WORKDIR /code

COPY localhost.cert /code/localhost.cert
COPY localhost.key /code/localhost.key
COPY main.py /code/main.py



# ENTRYPOINT ["uvicorn", "main:app", "--port=8000", "--host=0.0.0.0", "--forwarded-allow-ips='*'"]

ENTRYPOINT ["uvicorn", "main:app", "--port=8443", "--host=0.0.0.0", "--forwarded-allow-ips='*'", "--ssl-keyfile=localhost.key", "--ssl-certfile=localhost.cert"]

