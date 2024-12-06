#!/bin/bash

docker build -t nikitka22/myapp:2.0.0 .

docker login

docker push nikitka22/myapp:2.0.0