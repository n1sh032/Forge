from src.providers.gemini import GeminiProvider


provider = GeminiProvider()

response = provider.generate(
    "Reply with exactly: FORGE Gemini connection successful"
)

print(response)