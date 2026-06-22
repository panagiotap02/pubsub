# Message queue with NATS and Kubernetes

A cloud-native, event-driven architecture implementing the **Publisher-Subscriber (Pub/Sub)** pattern. This project features containerized Python applications coordinated via **Kubernetes** using **NATS Server** as the high-performance message broker.
* **Description:** *A cloud-native Pub/Sub architecture built with Python, NATS, Docker, and Kubernetes.*
* **Topics:** `kubernetes`, `nats`, `pubsub`, `python`, `docker`, `event-driven`
---

## System Architecture & Workflow

The system is split into three core components:
1. **NATS Broker:** The central nervous system that routes messages based on subjects.
2. **Publisher:** A service producing and broadcasting events/messages.
3. **Subscriber:** A service listening continuously for incoming messages on a specific channel.

The dynamic sequence diagram below illustrates how components interact inside the cluster in real-time:

```mermaid
sequenceDiagram
    autonumber
    participant Pub as Publisher Pod
    participant NATS as NATS Broker (Service)
    participant Sub as Subscriber Pod

    Note over Pub, Sub: Kubernetes Cluster Active
    Pub->>NATS: Publish Message (Subject: "updates")
    activate NATS
    NATS-->>Sub: Stream & Deliver Message
    deactivate NATS
    activate Sub
    Note over Sub: Process Message & Log Output
    deactivate Sub
 ```


## Structure

publisher/ — Contains the Python publisher script and its Dockerfile. Responsible for pushing messages to NATS.
subscriber/ — Contains the Python subscriber script and its Dockerfile. Listens to NATS channels and processes payloads.
k8s/ — Kubernetes manifests holding the deployment and service configurations for NATS, the publisher, and the subscriber.
test_connection/ — A standalone script environment (test.py) to easily verify broker connectivity.

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
