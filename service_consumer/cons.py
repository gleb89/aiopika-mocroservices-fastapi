import asyncio
from aio_pika import connect, IncomingMessage

from main import gg



async def on_message(message: IncomingMessage):
    title = message.body.decode('utf-8')
    await gg(title)
    


async def main(loop):
    # Perform connection
    connection = await connect(
        "amqp://user:bitnami@rabbit/", loop=loop
    )

    # Creating a channel
    channel = await connection.channel()

    # Declaring queue
    queue = await channel.declare_queue("hello")

    # Start listening the queue with name 'hello'
    await queue.consume(on_message, no_ack=True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))

    # we enter a never-ending loop that waits for data and
    # runs callbacks whenever necessary.
    print(" [*] Waiting for messages. To exit press CTRL+C")
    loop.run_forever()