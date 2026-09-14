from src.providers.openai import OpenAIProvider
from src.agents.critic import Critic
from src.agents.repair import Repair


provider = OpenAIProvider()

critic = Critic(provider)
repair = Repair(provider)


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


print("\n--- FIRST CRITIC REVIEW ---")

critique = critic.review(
    task,
    plan,
    files
)

print("Approved:", critique["approved"])
print("Issues:", critique["issues"])


if not critique["approved"]:

    print("\n--- REPAIRING ---")

    repaired = repair.repair(
        task,
        files,
        critic_feedback=critique,
        test_result=None
    )

    print("\n--- REPAIRED CODE ---")
    print(repaired)

    print("\n--- SECOND CRITIC REVIEW ---")

    second_critique = critic.review(
        task,
        plan,
        repaired["files"]
    )

    print("Approved:", second_critique["approved"])
    print("Issues:", second_critique["issues"])