#!/bin/sh
cp .env.example .env
docker-compose up  --build
docker-compose down
