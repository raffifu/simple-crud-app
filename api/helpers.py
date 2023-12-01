import os
from datetime import datetime
from kafka import KafkaProducer
from fastapi.responses import JSONResponse


def api_response(status, message, data=None):
    """Base response to create all return value standard."""
    json = {"status": status, "message": message, "timestamp": str(datetime.now())}

    if data:
        json["data"] = data

    return JSONResponse(status_code=status, content=json)


def save_to_file(filename, data):
    """Save data to filename."""
    directory = os.path.dirname(filename)

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(filename, "w") as f:
        f.write(data)


def send_to_kafka(topic, message):
    """Send message to kafka"""
    producer = KafkaProducer(bootstrap_servers="localhost:9092")

    producer.send(topic, message)

    producer.flush()
