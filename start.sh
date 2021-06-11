#/bin/bash

uvicorn main:app --port=8443 --host=0.0.0.0 --forwarded-allow-ips='*' --ssl-keyfile=localhost.key --ssl-certfile=localhost.cert

