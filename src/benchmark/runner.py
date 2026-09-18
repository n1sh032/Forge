import shutil
import tempfile
import time
from pathlib import Path

from src.agents.builder import Builder
from src.tools.file_writer import write_files
from src.tools.test_runner import run_tests


class BenchmarkRunner:
    def __init__(self, providers):
        self.providers = providers

    def run_task(self, provider_name, provider, benchmark):
        print()
        print("=" * 50)
        print("MODEL:", provider_name)
        print("TASK:", benchmark["name"])

        temp_dir = Path(
            tempfile.mkdtemp(
                prefix="forge_benchmark_"
            )
        )

        start_time = time.perf_counter()

        try:
            builder = Builder(provider)

            result = builder.build(
                benchmark["task"],
                {
                    "goal": benchmark["task"],
                    "requirements": [],
                    "steps": [],
                    "tests": benchmark["tests"]
                }
            )

            if not result:
                return {
                    "model": provider_name,
                    "task": benchmark["name"],
                    "success": False,
                    "latency": time.perf_counter() - start_time,
                    "error": "Builder returned no result."
                }

            write_files(
                result["files"],
                temp_dir
            )

            test_result = run_tests(
                temp_dir,
                benchmark["tests"]
            )

            latency = time.perf_counter() - start_time

            return {
                "model": provider_name,
                "task": benchmark["name"],
                "success": test_result["success"],
                "latency": latency,
                "tests": test_result
            }

        except Exception as e:
            return {
                "model": provider_name,
                "task": benchmark["name"],
                "success": False,
                "latency": time.perf_counter() - start_time,
                "error": str(e)
            }

        finally:
            shutil.rmtree(
                temp_dir,
                ignore_errors=True
            )

    def run_all(self, benchmarks):
        results = []

        for benchmark in benchmarks:
            for provider_name, provider in self.providers.items():

                result = self.run_task(
                    provider_name,
                    provider,
                    benchmark
                )

                results.append(result)

                print(
                    "Success:",
                    result["success"]
                )

                print(
                    "Latency:",
                    round(result["latency"], 2),
                    "seconds"
                )

        return results

    def calculate_statistics(self, results):
        statistics = {}

        for result in results:
            model = result["model"]

            if model not in statistics:
                statistics[model] = {
                    "total_tasks": 0,
                    "successful_tasks": 0,
                    "total_latency": 0
                }

            statistics[model]["total_tasks"] += 1

            if result["success"]:
                statistics[model]["successful_tasks"] += 1

            statistics[model]["total_latency"] += result["latency"]

        for model in statistics:
            data = statistics[model]

            data["success_rate"] = (
                data["successful_tasks"]
                / data["total_tasks"]
            )

            data["average_latency"] = (
                data["total_latency"]
                / data["total_tasks"]
            )

        return statistics