# Use a slim Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the subscriber script into the container
COPY subscriber.py .

# Install required Python packages
RUN pip install --no-cache-dir nats-py

# Run the subscriber script
CMD ["python", "subscriber.py"]
