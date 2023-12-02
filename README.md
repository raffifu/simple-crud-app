# Simple CRUD App
Simple CRUD App with kafka and monitoring in grafana

## Endpoint
- `/metrics` export metrics in the prometheus format
- `/api/v1/generate` Generate dummy csv
- `/api/v1/download` Download dummy csv
- `/api/v1/send_mq` Send message to kafka

## How to start
### Docker
1. Run the docker compose command
```sh
$ docker compose -f docker-compose.yml up -d
```

### Manual
1. Setup kafka running on your local, set the kafka url as environment variable `BOOTSTRAP_SERVER`
2. Create virtualenv in python
```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
```
3. Install the dependencies
```sh
$ pip3 install -r requirements.txt
```
4. Running the development server
```sh
$ uvicorn api:app --reload
```