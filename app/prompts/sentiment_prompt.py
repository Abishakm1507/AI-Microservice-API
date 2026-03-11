def build_sentiment_prompt(text: str) -> str:
    prompt = f"""
Analyze the sentiment of the following text.

Text:
{text}

Return only one word:
Positive, Negative, or Neutral.
"""

    return prompt