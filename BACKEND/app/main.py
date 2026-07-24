from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "name": "SOZENS AI",
        "version": "0.0.1",
        "status": "Running",
        "developer": "Lewis"
    }
