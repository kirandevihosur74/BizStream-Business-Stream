from fastapi import FastAPI, Request
import redis
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

app = FastAPI()
redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.get("/recommend")
def recommend(request: Request):
    logging.info(f"Received /recommend request from {request.client.host}")
    try:
        keys = redis_client.keys('*')
        logging.info(f"Found {len(keys)} businesses in Redis.")
        businesses = [json.loads(redis_client.get(k)) for k in keys]
        recommendations = sorted(businesses, key=lambda b: b['rating'], reverse=True)
        logging.info(f"Returning {len(recommendations)} recommendations.")
        return {"recommendations": recommendations}
    except Exception as e:
        logging.error(f"Error in /recommend: {e}")
        return {"recommendations": []} 