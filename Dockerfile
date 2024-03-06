# Use the official Python 3.9 image
FROM python:3.9

# Set the working directory
WORKDIR /code

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Install Redis
RUN apt-get update && \
    apt-get install -y redis-server

# Expose Redis port (default is 6379)
EXPOSE 8000 6379

WORKDIR /code/app

# Start the application and Redis
CMD redis-server --daemonize yes & uvicorn main:app --host 0.0.0.0 --port 8000 > uvicorn.log 2>&1 & exec huey_consumer.py tasks.huey
