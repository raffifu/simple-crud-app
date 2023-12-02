import os
from datetime import datetime
from aiokafka import AIOKafkaProducer
from fastapi.responses import JSONResponse

BOOTSTRAP_SERVER = os.getenv("BOOTSTRAP_SERVER", "localhost:9092")


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


async def send_to_kafka(topic, message):
    """Send message to kafka"""
    producer = AIOKafkaProducer(bootstrap_servers=BOOTSTRAP_SERVER)

    await producer.start()

    try:
        await producer.send_and_wait(topic, message)
    finally:
        await producer.stop()
