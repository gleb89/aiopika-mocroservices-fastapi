from fastapi import FastAPI

app = FastAPI(openapi_url="/listen/openapi.json", docs_url="/listen/docs")

@app.get('/listen')
def hh():
    return 'listen'