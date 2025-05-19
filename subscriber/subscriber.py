import asyncio
from nats.aio.client import Client as NATS

async def run():
    nc = NATS()

    try:
        print("Connecting to NATS at 'nats://my-nats:4222' ")
        await nc.connect("nats://my-nats:4222")
        print("Succesfully connected to NATS")

        async def message_handler(msg):
            subject = msg.subject
            data = msg.data.decode()
            print(f"Received message on '{subject}': {data}")

        print("Subscribing to 'updates' topic...")
        await nc.subscribe("updates", cb=message_handler)

        print("Listening for messages...") #(press Ctrl+C to exit)
        while True:
            await asyncio.sleep(1)

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        print("Closing connection...")
        await nc.close()
        print("Connection closed.")

if __name__ == '__main__':
    asyncio.run(run())
