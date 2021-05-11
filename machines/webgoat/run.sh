#!/bin/bash

docker run -p 127.0.0.1:9080:8080 -p 127.0.0.1:9081:9090 -e TZ=Europe/Amsterdam webgoat/goatandwolf
