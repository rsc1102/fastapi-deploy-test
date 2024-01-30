from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def check_status():
    return {"status":"web page deployed"}
