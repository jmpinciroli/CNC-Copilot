from fastapi import FastAPI

app = FastAPI(
    title="CNC Copilot API",
    version="0.1"
)

@app.get("/")
def home():
    return {
        "app": "CNC Copilot",
        "version": "0.1"
    }
