# Simple producer for rabbit_mq for getting depth of market data with FinamApi

## Brief instructions

To test:
1. run rabbit mq `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management `
2. start main.py `python main.py`

For complete cycle [consumer](https://github.com/snakerzr/Finam_market_data_consumer) and clickhouse is needed.

## .env file
Specify your finam `TOKEN` in .env file.  
`CLIENT_IDS` is not nessecary now.  
`RABBIT_MQ_HOST` = localhost if starting rabbitmq container locally.

## Docker build
Create producer image example:
```commandline
docker build -t producer:1 -f ./docker/Dockerfile .
```
or force fresh build
```commandline
docker build --no-cache -t producer:1 -f ./docker/Dockerfile .
```

start docker image
```commandline
docker run --rm -it --name producer_test -e TOKEN=your_finam_token -e RABBIT_MQ_HOST=rabbit_mq_host  producer:1 
```

