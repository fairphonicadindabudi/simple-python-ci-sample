from fastapi import FastAPI

app = FastAPI()

@app.get("/addition")
def addition(a: int = 0, b: int = 0):
    return {"result": a+b}