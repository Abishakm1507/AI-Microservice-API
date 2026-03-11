from fastapi import APIRouter
from app.models.schemas import SentimentRequest, SentimentResponse
from app.prompts.sentiment_prompt import build_sentiment_prompt
from app.services.llm_service import generate_response
from app.utils.logger import logger

router = APIRouter(prefix="/sentiment", tags=["Sentiment"])

@router.post("/", response_model=SentimentResponse)
def analyze_sentiment(request: SentimentRequest):

    logger.info("Sentiment analysis request")

    prompt = build_sentiment_prompt(request.text)

    sentiment = generate_response(prompt)

    logger.info(f"Sentiment result: {sentiment}")

    return SentimentResponse(sentiment=sentiment)