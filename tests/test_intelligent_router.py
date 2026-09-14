from src.providers.openai import OpenAIProvider
from src.providers.gemini import GeminiProvider
from src.router import Router


router = Router({
    "planner": OpenAIProvider(),
    "builder": GeminiProvider(),
    "critic": OpenAIProvider(),
    "repair": GeminiProvider()
})


task = "Create a Python calculator."


print("Planner:", router.select_provider("planner", task).model)
print("Builder:", router.select_provider("builder", task).model)
print("Critic:", router.select_provider("critic", task).model)
print("Repair:", router.select_provider("repair", task).model)