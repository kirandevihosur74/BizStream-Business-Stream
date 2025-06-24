# Verbizz: Business Matchmaker Platform

A real-time, containerized platform that matches businesses to user preferences using streaming Yelp business data. Built with Kafka, Redis, FastAPI, Streamlit, and Docker Compose.

---

## 🚀 Architecture Overview

```
Yelp Data → Kafka Producer → Kafka → ETL Consumer → Redis → FastAPI API → Streamlit Frontend
```

- **Kafka**: Streams business data in real time.
- **ETL Consumer**: Processes and loads data into Redis.
- **Redis**: Fast in-memory cache for business data.
- **FastAPI**: Serves recommendations via REST API.
- **Streamlit**: Interactive frontend dashboard.
- **Docker Compose**: Orchestrates all services for local development.

---

## 🗂️ Project Structure

```
producer/           # Kafka producer service
etl/                # ETL consumer service
api/                # FastAPI recommendation API
frontend/           # Streamlit frontend
run_all.sh          # Script to build and run all services
README.md           # This file
docker-compose.yml  # Multi-service orchestration
```

---

## ⚡ Quick Start

### 1. Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- (Optional) [Python 3.11+](https://www.python.org/) and `venv` for local development

### 2. Build & Run All Services

```sh
./run_all.sh
```
Or manually:
```sh
docker-compose up --build
```

### 3. Access the Application
- **Frontend:** [http://localhost:8501](http://localhost:8501)
- **API:** [http://localhost:8000/recommend](http://localhost:8000/recommend)

---

## 🛠️ Development (Optional: Local Python)

1. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install all requirements:
   ```sh
   pip install -r producer/requirements.txt -r etl/requirements.txt -r api/requirements.txt -r frontend/requirements.txt
   ```
3. Run each service in a separate terminal:
   - Producer: `python producer/producer.py`
   - ETL: `python etl/etl_consumer.py`
   - API: `uvicorn api/recommendation_api:app --reload --host 0.0.0.0 --port 8000`
   - Frontend: `streamlit run frontend/app.py`

---

## 🧩 Configuration
- All service dependencies are managed via `requirements.txt` in each service directory.
- Kafka and Zookeeper use Bitnami images for reliability.
- Redis is used for fast, in-memory caching.

---

## 📝 Customization & Extending
- Add more sample or real Yelp data in `producer/producer.py`.
- Enhance matching logic in `etl/etl_consumer.py` and `api/recommendation_api.py`.
- Improve frontend features in `frontend/app.py` (filters, search, maps, etc).

---

## 🐳 Docker Compose Reference
- `run_all.sh` — builds and starts all services
- `docker-compose up` — starts services
- `docker-compose down` — stops and removes services

---

## 🛡️ Observability & Reliability
- Logging is enabled in all Python services.
- Kafka and Redis are production-grade and scalable.
- For production, consider adding monitoring (Prometheus, Grafana) and error alerting.

---

## 📄 License
MIT (or your preferred license)

---

## 🙋‍♂️ Need Help?
Open an issue or contact the maintainer.