from fastapi import APIRouter
from app.models.schemas import SummarizeRequest, SummarizeResponse
from app.prompts.summarize_prompt import build_summary_prompt
from app.services.llm_service import generate_response
from app.utils.logger import logger

router = APIRouter(prefix="/summarize", tags=["Summarize"])

@router.post("/", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):

    logger.info(f"Summarize request received")

    prompt = build_summary_prompt(request.text)

    summary = generate_response(prompt)

    logger.info(f"Summary generated")

    return SummarizeResponse(summary=summary)