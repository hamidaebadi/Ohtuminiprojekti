#!/bin/bash

# käynnistetään Flask-palvelin taustalle
flask run 

# odetetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000/ping)" != "200" ]]; 
  do sleep 1; 
done

# suoritetaan testit
robot src/tests

status=$?

# pysäytetään Flask-palvelin portissa 5000
kill $(lsof -t -i:5000)

exit $status
