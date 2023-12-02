import os
import asyncio
from aiokafka import AIOKafkaConsumer
from prometheus_client import Counter

BOOTSTRAP_SERVER = os.getenv("BOOTSTRAP_SERVER", "localhost:9092")

message_counter = Counter("received_messages", "Received messages from kafka")


async def consumer():
    consumer = AIOKafkaConsumer("api-events", bootstrap_servers=BOOTSTRAP_SERVER)

    connected = False
    while not connected:
        try:
            await consumer.start()
            connected = True
            print("Connected to Kafka!")
        except Exception as e:
            print(f"Connection failed: {e}")
            await asyncio.sleep(2)

    try:
        async for _ in consumer:
            message_counter.inc()
    finally:
        await consumer.stop()
