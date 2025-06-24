FROM python:3.11-slim
WORKDIR /app
COPY recommendation_api.py .
RUN pip install fastapi redis uvicorn
CMD ["uvicorn", "recommendation_api:app", "--host", "0.0.0.0", "--port", "8000"] 