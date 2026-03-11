from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.utils.logger import logger


async def global_exception_handler(request: Request, exc: Exception):

    logger.error(f"Unhandled error: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "Something went wrong"
        },
    )