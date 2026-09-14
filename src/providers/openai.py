import os

from dotenv import load_dotenv
from openai import OpenAI

from src.providers.base import BaseProvider


load_dotenv()


class OpenAIProvider(BaseProvider):
    def __init__(self, model="gpt-5"):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.model = model

    def generate(self, prompt):
        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )

        return response.output_text