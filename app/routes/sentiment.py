from fastapi import APIRouter
from app.models.schemas import SentimentRequest, SentimentResponse
from app.prompts.sentiment_prompt import build_sentiment_prompt
from app.services.llm_service import generate_response

router = APIRouter(prefix="/sentiment", tags=["Sentiment"])


@router.post("/", response_model=SentimentResponse)
def analyze_sentiment(request: SentimentRequest):

    prompt = build_sentiment_prompt(request.text)

    sentiment = generate_response(prompt)

    return SentimentResponse(sentiment=sentiment)