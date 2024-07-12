
# Kaspa price rometheus exporter
Note: special request from my friend Dave

## Install app

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

## Prometheus source setup

```yaml
scrape_configs:
  - job_name: 'kaspa_price'
    scrape_interval: 2h
    static_configs:
      - targets: ['localhost:8111']
```