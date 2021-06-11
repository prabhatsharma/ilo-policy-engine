#!/bin/bash

openssl genrsa -aes256 -passout pass:somepassword -out server.pass.key 4096

openssl rsa -passin pass:somepassword -in server.pass.key -out server.key 

openssl req -new -key server.key -out server.csr -config csr.conf

openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt