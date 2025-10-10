from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUEST_COUNT = Counter('request_count', 'Total number of requests')

@app.route('/')
def hello_world():
    REQUEST_COUNT.inc()
    # Simulate CPU-intensive work for each HTTP request
    import time
    start = time.time()
    while time.time() - start < 0.1:  # 100ms of CPU work per request
        x = sum(i*i for i in range(1000))
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
