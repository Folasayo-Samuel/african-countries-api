from prometheus_client import Counter, Histogram, generate_latest
from prometheus_client import REGISTRY
from fastapi import Request
import time
from loguru import logger

# Create a counter for counting requests
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests', ['method', 'endpoint', 'http_status'])

# Create a histogram to measure request durations
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency in seconds', ['endpoint'])

# Middleware to collect metrics
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    REQUEST_LATENCY.labels(endpoint=request.url.path).observe(process_time)
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path, http_status=response.status_code).inc()

    return response

# Define the /metrics endpoint for Prometheus scraping
async def get_metrics():
    return generate_latest(REGISTRY)

# Setup basic logging
logger.add("logs/app.log", rotation="1 MB", retention="10 days", compression="zip")
