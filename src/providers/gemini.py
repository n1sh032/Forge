import os

from dotenv import load_dotenv
from google import genai

from src.providers.base import BaseProvider


load_dotenv()


class GeminiProvider(BaseProvider):
    def __init__(self, model="gemini-3.5-flash-lite"):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )
        self.model = model

    def generate(self, prompt):
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text