from fastapi import FastAPI

app = FastAPI(title="Hackathon App")


@app.get("/")
def root():
    return {"status": "ok", "message": "Hello from hackathon!"}


@app.get("/health")
def health():
    return {"status": "healthy"}