from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    event = {"user_id": random.randint(0, 99)}
    producer.send('user_events', event)
    print("Produced:", event)
    time.sleep(1)
