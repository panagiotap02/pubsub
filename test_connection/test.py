import socket

host = "localhost"
port = 4222

try:
    with socket.create_connection((host, port), timeout=10):
        print(f"Successfully connected to {host}:{port}")
except Exception as e:
    print(f"Failed to connect to {host}:{port} - {e}")

