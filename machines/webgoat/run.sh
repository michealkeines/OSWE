#!/bin/bash

docker run -p 127.0.0.1:9001:8080 -p 127.0.0.1:9002:9090 -e TZ=Europe/Amsterdam webgoat/goatandwolf
