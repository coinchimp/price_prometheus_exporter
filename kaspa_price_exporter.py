import time
import requests
from prometheus_client import start_http_server, Gauge

# Define the Prometheus Gauge metric
kaspa_price_gauge = Gauge('kaspa_price', 'Current price of Kaspa (KAS) in USD')

def fetch_kaspa_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=kaspa&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data['kaspa']['usd']
    return price

def update_kaspa_price():
    while True:
        price = fetch_kaspa_price()
        kaspa_price_gauge.set(price)
        print(f"Updated Kaspa price: {price} USD")
        time.sleep(7200)  # Sleep for 2 hours

if __name__ == "__main__":
    # Start the Prometheus HTTP server on port 8111
    start_http_server(8111)
    print("Prometheus metrics server started on port 8111")
    
    # Start updating the Kaspa price
    update_kaspa_price()
