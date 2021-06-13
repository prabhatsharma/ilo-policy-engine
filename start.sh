#/bin/bash

uvicorn main:app --port=8443 --host=0.0.0.0 --forwarded-allow-ips='*' --ssl-keyfile=cert/server.key --ssl-certfile=cert/server.crt

