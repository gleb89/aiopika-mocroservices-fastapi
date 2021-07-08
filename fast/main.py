
import asyncio
from aio_pika import connect, Message

from fastapi import FastAPI

app = FastAPI(openapi_url="/fast/openapi.json", docs_url="/fast/docs")


@app.get('/fast')
def hh():
    return 'fast'

async def main(y):
    # Perform connection
    connection = await connect(
        "amqp://user:bitnami@rabbit/"
    )

    # Creating a channel
    channel = await connection.channel()

    # Sending the message
    await channel.default_exchange.publish(
        Message(str(y).encode("utf-8")),
        routing_key="hello",
    )

    print(" [x] Sent 'Hello World!'")

    await connection.close()

@app.get("/fast/tt")
async def read_root(y:str):
    await main(y)
    return {"Hello": "World"}



