def build_chat_prompt(user_message: str) -> str:
    prompt = f"""
You are a helpful AI assistant.

User message:
{user_message}

Respond in a clear and conversational way.
"""

    return prompt