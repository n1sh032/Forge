from src.providers.openai import OpenAIProvider
from src.agents.critic import Critic


provider = OpenAIProvider()
critic = Critic(provider)

task = "Create a Python program that prints exactly: Hello from FORGE"

plan = {
    "goal": "Create a simple Python greeting program.",
    "requirements": [
        "Print exactly Hello from FORGE"
    ]
}

files = [
    {
        "path": "main.py",
        "content": 'print("Hello")'
    }
]

result = critic.review(
    task,
    plan,
    files
)

print("\n--- CRITIC RESULT ---")
print(result)