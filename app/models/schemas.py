from pydantic import BaseModel

# Chat
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str


# Summarization
class SummarizeRequest(BaseModel):
    text: str

class SummarizeResponse(BaseModel):
    summary: str


# Sentiment Analysis
class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str