import random
import time

from flask import Flask, Response
from prometheus_client import (
    Counter,
    Gauge,
    Histogram,
    generate_latest,
    start_http_server,
)

app = Flask(__name__)

# Custom metrics
REQUEST_COUNT = Counter(
    "http_requests_total", "Total HTTP Requests", ["method", "endpoint", "status"]
)
REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds", "HTTP request latency", ["endpoint"]
)
TEMPERATURE_GAUGE = Gauge("temperature_celsius", "Current temperature in Celsius")
ERROR_COUNT = Counter("http_errors_total", "Total HTTP Errors", ["type"])


@app.route("/")
def home():
    REQUEST_COUNT.labels(method="GET", endpoint="/", status="200").inc()

    with REQUEST_LATENCY.labels(endpoint="/").time():
        # Simulates running aplication
        time.sleep(random.uniform(0.1, 0.3))
        temperature = random.uniform(20, 30)
        TEMPERATURE_GAUGE.set(temperature)

        # Simulates error
        if random.random() < 0.1:
            ERROR_COUNT.labels(type="500").inc()
            return "Erro interno", 500

        return f"Temperatura atual: {temperature:.2f}°C"


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")


if __name__ == "__main__":
    metric_server_port = 8000
    start_http_server(metric_server_port)
    # Run flask in port 5000
    app.run(host="0.0.0.0", port=5000)
