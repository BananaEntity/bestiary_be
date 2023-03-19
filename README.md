# run local

## build docker image
docker compose build

## run
docker compose --env-file .\resource\.env up -d

## stop
docker compose stop
