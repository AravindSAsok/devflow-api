from fastapi import FastAPI

app = FastAPI(title="DevFlow API")


@app.get("/")
def home():
    return {
        "message": "Bro, CI/CD is coming!",
        "app": "DevFlow API",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}