from src.providers.openai import OpenAIProvider
from src.router import Router


planner = OpenAIProvider()
builder = OpenAIProvider()
critic = OpenAIProvider()
repair = OpenAIProvider()

router = Router({
    "planner": planner,
    "builder": builder,
    "critic": critic,
    "repair": repair
})


print(
    router.get_provider("planner").model
)

print(
    router.get_provider("builder").model
)

print(
    router.get_provider("critic").model
)

print(
    router.get_provider("repair").model
)