from src.providers.openai import OpenAIProvider
from src.orchestrator import Orchestrator


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

    provider = OpenAIProvider()
    forge = Orchestrator(provider)

    forge.run(task)


if __name__ == "__main__":
    main()