from fastapi import FastAPI

from app.routes import chat
from app.routes import summarize
from app.routes import sentiment

app = FastAPI(
    title="AI Microservice API",
    version="1.0"
)

app.include_router(chat.router)
app.include_router(summarize.router)
app.include_router(sentiment.router)


@app.get("/")
def root():
    return {"message": "AI Microservice API running"}