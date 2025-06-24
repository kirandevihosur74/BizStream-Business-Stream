import json
import logging
from kafka import KafkaConsumer
import redis

logging.basicConfig(level=logging.INFO)

consumer = KafkaConsumer(
    'yelp-businesses',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='etl-group'
)

redis_client = redis.Redis(host='redis', port=6379, db=0)

def process_and_store():
    for message in consumer:
        try:
            business = message.value
            # Example transformation: normalize name
            business['name'] = business['name'].strip().title()
            redis_client.set(business['id'], json.dumps(business))
            logging.info(f"Stored business {business['id']} in Redis")
        except Exception as e:
            logging.error(f"Error processing message: {e}")

if __name__ == "__main__":
    process_and_store() 