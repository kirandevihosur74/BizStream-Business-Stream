import json
import time
from kafka import KafkaProducer
import logging

logging.basicConfig(level=logging.INFO)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_yelp_businesses():
    # Simulated Yelp data stream (replace with real API calls in production)
    sample_data = [
        {
            "id": "abc123",
            "name": "Test Restaurant",
            "rating": 4.5,
            "address": "123 Main St",
            "category": "Italian",
            "city": "New York",
            "state": "NY",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "phone": "123-456-7890",
            "price": "$$"
        },
        # Add more sample businesses as needed
    ]
    for business in sample_data:
        yield business

def stream_yelp_data():
    for business in get_yelp_businesses():
        try:
            producer.send('yelp-businesses', business)
            producer.flush()
            logging.info(f"Sent business: {business['id']}")
            time.sleep(1)  # Simulate real-time streaming
        except Exception as e:
            logging.error(f"Failed to send business: {e}")

if __name__ == "__main__":
    stream_yelp_data() 