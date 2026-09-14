from src.providers.openai import OpenAIProvider
from src.providers.gemini import GeminiProvider
from src.orchestrator import Orchestrator
from src.router import Router
from src.providers.gemini import GeminiProvider



def main():
    print("=" * 35)
    print("         FORGE")
    print("AI Software Builder")
    print("=" * 35)

    task = input("\nWhat do you want FORGE to build?\n\n> ")

    if not task.strip():
        print("No task entered.")
        return

    print("\nStarting FORGE...")

    planner_provider = OpenAIProvider()
    builder_provider = GeminiProvider()
    critic_provider = OpenAIProvider()
    repair_provider = GeminiProvider()

    router = Router({
        "planner": planner_provider,
        "builder": builder_provider,
        "critic": critic_provider,
        "repair": repair_provider
    })

    forge = Orchestrator(router)

    forge.run(task)


if __name__ == "__main__":
    main()