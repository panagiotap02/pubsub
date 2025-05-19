import asyncio
from nats.aio.client import Client as NATS

async def run():
    nc = NATS()

    try:
        # Connect to NATS server (service name in Kubernetes)
        await nc.connect(
            servers=["nats://my-nats:4222"],
            connect_timeout=5,
            max_reconnect_attempts=5,
            reconnect_time_wait=2
        )
        print("Succesfully connected to NATS")

        # Publish a single message
        message = b"Hello from publisher!"
        print(f"Publishing message: {message.decode()}")
        await nc.publish("updates", message)

    except Exception as e:
        print(f"Failed to publish message: {e}")

    finally:
        print("Closing connection...")
        await nc.close()
        print("Connection closed.")

if __name__ == "__main__":
    asyncio.run(run())
