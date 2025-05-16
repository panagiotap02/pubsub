# Use a slim Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the publisher script into the container
COPY publisher.py .

# Install required Python packages
RUN pip install --no-cache-dir nats-py

# Run the publisher script
CMD ["python", "publisher.py"]
