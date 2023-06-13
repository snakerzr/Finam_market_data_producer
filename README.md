# Simple producer for rabbit_mq for getting depth of market data with FinamApi

## Brief instructions

To test:
1. run rabbit mq `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management `
2. start main.py `python main.py`

For complete cycle consumer (link) and clickhouse is needed.

## .env file
Specify your finam `TOKEN` in .env file.  
`CLIENT_IDS` is not nessecary now.  
`RABBIT_MQ_HOST` = localhost if starting rabbitmq container locally.

## Docker build
Create producer image example:
```
docker build -t producer:1 -f ./docker/Dockerfile .
```
or force fresh build
```
docker build --no-cache -t producer:1 -f ./docker/Dockerfile .
```


