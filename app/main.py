from fastapi import FastAPI

app = FastAPI(
    title="AI Microservice API",
    description="Microservice for AI powered APIs",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "AI Microservice API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}