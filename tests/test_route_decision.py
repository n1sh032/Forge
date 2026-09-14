from src.providers.openai import OpenAIProvider
from src.providers.gemini import GeminiProvider
from src.router import Router


router = Router({
    "openai": OpenAIProvider(),
    "gemini": GeminiProvider()
})


tasks = [
    "Print Hello World",
    "Create a Python calculator",
    "Build a REST API with authentication"
]


for task in tasks:
    print()
    print("=" * 40)
    print("TASK:", task)

    for agent in ["planner", "builder", "critic", "repair"]:
        decision = router.route(agent, task)

        print()
        print("Agent:", agent)
        print("Complexity:", decision["complexity"])
        print("Scores:", decision["scores"])
        print("Selected:", decision["provider_name"])
        print("Score:", decision["score"])