from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/ping')
def ping():
    return {"status": "ok"}

@app.route('/count')
def count():
    count = r.incr('hits')
    return {"visits": count}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
