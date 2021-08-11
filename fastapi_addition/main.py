from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def index():
    return "Simple Addition API"

@app.get("/addition")
def addition(a: int = Query(None), b: int = Query(None)):
    if not a or not b:
        return {
            "status": "error",
            "message": "Require 'a' and 'b' query parameter and must be integer"
        }
    return {"result": a+b}