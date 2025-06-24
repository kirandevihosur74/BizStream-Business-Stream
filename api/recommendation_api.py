from fastapi import FastAPI
import redis
import json

app = FastAPI()
redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.get("/recommend")
def recommend():
    # Fetch all businesses and return top 5 by rating
    keys = redis_client.keys('*')
    businesses = [json.loads(redis_client.get(k)) for k in keys]
    recommendations = sorted(businesses, key=lambda b: b['rating'], reverse=True)[:5]
    return {"recommendations": recommendations} 