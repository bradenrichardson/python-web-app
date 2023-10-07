from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/multiply/")
async def multiply(first: int, second: int):
    result = first * second
    return {"result" : f"{result}" }