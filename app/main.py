from fastapi import FastAPI

app = FastAPI(
    title="Azure DevOps Showcase API",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/api/message")
def get_message():
    return {"message": "Hello from the Azure DevOps Showcase API!"}


@app.get("/api/version")
def get_version():
    return {"version": "1.0.0"}
