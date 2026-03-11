from fastapi import FastAPI
from app.routes import chat, summarize, sentiment
from app.utils.error_handler import global_exception_handler

app = FastAPI(
    title="AI Microservice API",
    version="1.0"
)

app.include_router(chat.router)
app.include_router(summarize.router)
app.include_router(sentiment.router)

app.add_exception_handler(Exception, global_exception_handler)

@app.get("/")
def root():
    return {"message": "AI Microservice API running"}