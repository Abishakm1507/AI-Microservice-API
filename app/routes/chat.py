from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.prompts.chat_prompt import build_chat_prompt
from app.services.llm_service import generate_response
from app.utils.logger import logger

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    logger.info(f"Chat request: {request.message}")

    prompt = build_chat_prompt(request.message)

    ai_response = generate_response(prompt)

    logger.info(f"Chat response: {ai_response}")

    return ChatResponse(response=ai_response)