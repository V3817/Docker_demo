## 🚀 Flask + Redis Dockerized App

This project demonstrates how to run a simple Flask web application that uses Redis to count how many times a user has visited the homepage. Both services are containerized using Docker and orchestrated with Docker Compose.

---

### 📁 Project Structure

```
.
├── app.py                # Flask application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker image for Flask app
├── docker-compose.yml    # Defines multi-container setup
└── README.md             # Project documentation (you are here!)
```

---

### 🐍 Tech Stack

* **Flask**: Python micro web framework
* **Redis**: In-memory data store
* **Docker**: Containerization platform
* **Docker Compose**: Tool for defining and running multi-container Docker apps

---

### 🛠️ Setup Instructions

#### ✅ 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

#### ✅ 2. Build and run the containers

```bash
docker compose up --build
```

This will:

* Build the Flask app image using the `Dockerfile`
* Pull the Redis image
* Start both containers
* Map Flask on `localhost:8000`

---

### 🌐 Access the Web App

Open your browser and navigate to:

```
http://localhost:8000
```

You’ll see a message like:

```
Hello User I have seen you 1 times
```

Refresh the page to see the counter increase!

---

### 🧪 Test Redis Connection

Redis is used to store the visit count. Flask will keep trying to connect if Redis isn’t ready, thanks to a retry mechanism in `get_hit_count()`.

---

### 📦 Docker Commands

* **Stop containers**:

  ```bash
  docker compose stop
  ```

* **Start containers again**:

  ```bash
  docker compose start
  ```

* **Rebuild everything**:

  ```bash
  docker compose up --build
  ```

---

### 📄 `docker-compose.yml` (Explained)

```yaml
services:
  web:
    build: .
    ports:
      - "8000:5000"
    depends_on:
      - redis

  redis:
    image: redis
```

* **web**: Runs the Flask app
* **redis**: Official Redis image
* **depends\_on**: Ensures Redis starts before Flask

---

### 💡 Bonus Tips

* No need for `version:` in Docker Compose v2+
* To persist Redis data across restarts, consider using a volume
* Use environment variables to make Redis host configurable

---

### 🧼 To Clean Up

Stop and remove all containers:

```bash
docker compose down
```

