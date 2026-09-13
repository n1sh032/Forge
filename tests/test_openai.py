from src.providers.openai import OpenAIProvider


provider = OpenAIProvider()

response = provider.generate(
    "Reply with exactly: FORGE connection successful"
)

print(response)