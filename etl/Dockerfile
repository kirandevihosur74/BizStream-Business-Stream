FROM python:3.11-slim
WORKDIR /app
COPY etl_consumer.py .
RUN pip install kafka-python redis
CMD ["python", "etl_consumer.py"] 