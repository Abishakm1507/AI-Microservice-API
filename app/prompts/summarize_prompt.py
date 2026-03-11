def build_summary_prompt(text: str) -> str:
    prompt = f"""
You are an expert text summarizer.

Summarize the following text in 3–4 concise sentences.

Text:
{text}
"""

    return prompt