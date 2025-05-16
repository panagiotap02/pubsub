
# Messagequeue with NATS and Kubernetes

## Structure

- `publisher/` — Publishes messages to NATS
- `subscriber/` — Subscribes and listens to NATS messages
- `k8s/` — Kubernetes deployment and service configs

## Usage

1. Build Docker images (inside Minikube):
   ```bash
   eval $(minikube docker-env)
   docker build -t publisher-app:latest ./publisher
   docker build -t subscriber-app:latest ./subscriber
   ```

2. Deploy to Kubernetes:
   ```bash
   kubectl apply -f k8s/
   ```

3. Port-forward NATS (optional):
   ```bash
   kubectl port-forward service/my-nats 4222:4222
   ```

4. Check logs:
   ```bash
   kubectl logs -l app=subscriber
   kubectl logs -l app=publisher
   ```
