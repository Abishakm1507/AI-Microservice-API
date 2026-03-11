from app.services.llm_service import generate_response

prompt = "Explain artificial intelligence simply"

response = generate_response(prompt)

print(response)