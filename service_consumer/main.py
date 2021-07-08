from fastapi import FastAPI

from config.db import metadata, engine, database
from config.repo import Case

app = FastAPI(openapi_url="/service_consumer/openapi.json", docs_url="/service_consumer/docs")

metadata.create_all(engine)

app.state.database = database

@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()



@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

@app.post('/service_consumer')
async def hh(title:str):
    tt = Case(title=title)
    return await tt.save()

@app.get('/service_consumer/all')
async def hh():
    tt = await Case.objects.all()
    return tt


async def gg(title):
    await database.connect()
    tt = Case(title=title)
    await tt.save()
    await database.disconnect()