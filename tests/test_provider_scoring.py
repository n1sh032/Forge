from src.providers.openai import OpenAIProvider
from src.providers.gemini import GeminiProvider
from src.router import Router


openai = OpenAIProvider()
gemini = GeminiProvider()

router = Router({
    "planner": openai,
    "builder": gemini,
    "critic": openai,
    "repair": gemini
})


tasks = [
    "Print Hello World",
    "Create a Python calculator",
    "Build a REST API with authentication",
    "Build a machine learning classifier"
]


for task in tasks:
    print()
    print("TASK:", task)
    print("COMPLEXITY:", router.classify_task(task))

    for agent in ["planner", "builder", "critic", "repair"]:
        provider = router.select_provider(
            agent,
            task
        )

        print(
            agent,
            "->",
            provider.__class__.__name__
        )