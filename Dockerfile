FROM --platform=linux/amd64 python:3.8-slim-buster

# Install Firefox and geckodriver
RUN apt-get update && apt-get install -y firefox-esr && \
    apt-get install -y wget && \
    wget -q https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz && \
    tar -xzf geckodriver-v0.30.0-linux64.tar.gz && \
    rm geckodriver-v0.30.0-linux64.tar.gz && \
    chmod +x geckodriver && \
    mv geckodriver /usr/local/bin/

# Install Python dependencies
WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# Copy application code
COPY . /app

# Set environment variable
ENV FLASK_APP=app.py

# Expose the port
EXPOSE 8080

# Start the application
CMD ["python", "app.py"]
