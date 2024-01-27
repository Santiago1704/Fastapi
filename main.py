from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"msn":"Hola Mundo"}
