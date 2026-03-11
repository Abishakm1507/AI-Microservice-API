from groq import Groq
from app.utils.config import GROQ_API_KEY
from app.utils.logger import logger

client = Groq(api_key=GROQ_API_KEY)


def generate_response(prompt: str) -> str:

    try:

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        return completion.choices[0].message.content

    except Exception as e:

        logger.error(f"LLM error: {str(e)}")

        return "AI service temporarily unavailable."