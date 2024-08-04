from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/omg")
async def sayOmg():
        return {"data": "Oh my F***ing god it is working"}