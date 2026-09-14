from src.providers.openai import OpenAIProvider
from src.providers.gemini import GeminiProvider
from src.orchestrator import Orchestrator
from src.router import Router


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

    openai_provider = OpenAIProvider()
    gemini_provider = GeminiProvider()

    router = Router({
        "openai": openai_provider,
        "gemini": gemini_provider
    })

    forge = Orchestrator(router)

    forge.run(task)


if __name__ == "__main__":
    main()