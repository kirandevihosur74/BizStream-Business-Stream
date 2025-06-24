from faker import Faker
import time
import json
from kafka import KafkaProducer
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def stream_fake_businesses():
    while True:
        business = {
            "id": fake.uuid4(),
            "name": fake.company(),
            "address": fake.address(),
            "city": fake.city(),
            "state": fake.state_abbr(),
            "rating": round(fake.random.uniform(1, 5), 1),
            "category": fake.job(),
        }
        try:
            logging.info(f"Sending fake business to Kafka: {business['id']}")
            producer.send('yelp-businesses', business)
            producer.flush()
            logging.info(f"Sent business: {business['id']}")
        except Exception as e:
            logging.error(f"Failed to send business: {e}")
        time.sleep(1)

if __name__ == "__main__":
    logging.info("Starting fake business data producer...")
    stream_fake_businesses() 