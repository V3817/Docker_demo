import time
import redis
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Connect to Redis server
cache = redis.Redis(host='redis', port=6379)  # 'redis' is the hostname (for Docker networking)

def get_hit_count():
    """Function to get and increment the hit counter from Redis."""
    retries = 5  # Number of retries if Redis connection fails
    while True:
        try:
            # Attempt to increment the 'hits' key in Redis
            return cache.incr("hits")  # 'incr' increments the value and returns it
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc  # Raise the exception if all retries fail
            retries -= 1
            time.sleep(0.5)  # Wait before retrying

@app.route("/")
def hello():
    """Root endpoint that returns visit count."""
    count = get_hit_count()
    return f"Hello User, I have seen you {count} times\n"
