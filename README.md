# prometheus-example

[![PyPI - Version](https://img.shields.io/pypi/v/prometheus-example.svg)](https://pypi.org/project/prometheus-example)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/prometheus-example.svg)](https://pypi.org/project/prometheus-example)

-----

## Installation

```console
```

## Configuration

prometheus.yml

```bash
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'python-app'
    metrics_path: '/metrics'
    static_configs:
      - targets: ['host.docker.internal:8000'] # Para Linux usar['localhost:8000']
```

## Usage

1. Start python application

```console
python app.py
```

2. Start services with Docker

```console
docker-compose up -d
```

3. Access services:
Prometheus: http://localhost:9090
Grafana: http://localhost:3000 (usuário: admin, senha: admin)

Add Prometheus datasource in grafana (URL: http://prometheus:9090)

Import dashboard from JSON file


## License

`prometheus-example` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
