from pathlib import Path

from src.agents.planner import Planner
from src.agents.builder import Builder
from src.agents.repair import Repair
from src.tools.file_writer import write_files
from src.tools.test_runner import run_tests


MAX_AGENT_CALLS = 5
MAX_REPAIR_ATTEMPTS = 2


class Orchestrator:
    def __init__(self, provider):
        self.planner = Planner(provider)
        self.builder = Builder(provider)
        self.repair = Repair(provider)

    def run(self, task):
        agent_calls = 0
        repair_attempts = 0

        print("\n--- PLANNING ---")

        if agent_calls >= MAX_AGENT_CALLS:
            print("Maximum agent calls reached.")
            return

        plan = self.planner.make_plan(task)
        agent_calls += 1

        if not plan:
            print("Planning failed.")
            return

        print("\n--- BUILDING ---")

        if agent_calls >= MAX_AGENT_CALLS:
            print("Maximum agent calls reached.")
            return

        result = self.builder.build(task, plan)
        agent_calls += 1

        if not result:
            print("Building failed.")
            return

        project_dir = Path("generated_project")

        write_files(
            result["files"],
            project_dir
        )

        while True:
            print("\n--- TESTING ---")

            test_result = run_tests(project_dir)

            if test_result["success"]:
                print("\nFORGE SUCCESS")
                print("The generated project passed its tests.")
                return

            print("\nTEST FAILED")
            print(test_result["error"])

            if repair_attempts >= MAX_REPAIR_ATTEMPTS:
                print("\nMaximum repair attempts reached.")
                print("FORGE stopped.")
                return

            if agent_calls >= MAX_AGENT_CALLS:
                print("\nMaximum agent calls reached.")
                print("FORGE stopped.")
                return

            print("\n--- REPAIRING ---")

            repaired = self.repair.repair(
                task,
                result["files"],
                test_result
            )

            agent_calls += 1
            repair_attempts += 1

            if not repaired:
                print("Repair failed.")
                return

            result = repaired

            write_files(
                result["files"],
                project_dir
            )

            print(
                f"Repair attempt: "
                f"{repair_attempts}/{MAX_REPAIR_ATTEMPTS}"
            )

        print(f"Agent calls: {agent_calls}/{MAX_AGENT_CALLS}")
        