from fastapi import FastAPI
from BACKEND.services.analysis import analyze_market
app = FastAPI(
    title="SOZENS AI",
    description="AI Trading Assistant",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "name": "SOZENS AI",
        "version": "0.1.0",
        "developer": "Lewis",
        "status": "🟢 Online",
        "mission": "Help traders make better decisions using AI."
    }

@app.get("/analysis")
def analysis():
    return analyze_market()