# Use lightweight Python 3.7 base image
FROM python:3.7-alpine

# Set working directory
WORKDIR /code

# Environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0  

# Copy everything into the container
COPY . .

# Install build dependencies for pip packages (needed on Alpine)
RUN apk add --no-cache gcc musl-dev libffi-dev && \
    pip install --no-cache-dir -r requirements.txt

# Expose Flask's default port
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]
