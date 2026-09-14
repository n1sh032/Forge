from src.providers.openai import OpenAIProvider
from src.providers.gemini import GeminiProvider
from src.router import Router


router = Router({
    "planner": OpenAIProvider(),
    "builder": GeminiProvider(),
    "critic": OpenAIProvider(),
    "repair": GeminiProvider()
})


tasks = [
    "Print Hello World",
    "Create a Python calculator",
    "Build a CSV file organizer",
    "Create a REST API with authentication",
    "Build a machine learning classifier"
]


for task in tasks:
    complexity = router.classify_task(task)

    print()
    print("Task:", task)
    print("Complexity:", complexity)