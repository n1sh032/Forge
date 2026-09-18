from src.providers.openai import OpenAIProvider
from src.providers.gemini import GeminiProvider
from src.benchmark.runner import BenchmarkRunner
from src.benchmark.tasks import BENCHMARK_TASKS


def main():
    providers = {
        "openai": OpenAIProvider(),
        "gemini": GeminiProvider()
    }

    runner = BenchmarkRunner(providers)

    results = runner.run_all(
        BENCHMARK_TASKS
    )

    statistics = runner.calculate_statistics(
        results
    )

    print()
    print("=" * 50)
    print("BENCHMARK SUMMARY")
    print("=" * 50)

    for model, data in statistics.items():
        print()
        print("Model:", model)

        print(
            "Tasks passed:",
            f"{data['successful_tasks']}/"
            f"{data['total_tasks']}"
        )

        print(
            "Success rate:",
            f"{data['success_rate'] * 100:.1f}%"
        )

        print(
            "Average latency:",
            f"{data['average_latency']:.2f}s"
        )


if __name__ == "__main__":
    main()