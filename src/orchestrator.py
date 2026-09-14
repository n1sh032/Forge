from pathlib import Path

from src.agents.planner import Planner
from src.agents.builder import Builder
from src.agents.critic import Critic
from src.agents.repair import Repair
from src.tools.file_writer import write_files
from src.tools.test_runner import run_tests
from src.router import Router


MAX_AGENT_CALLS = 10
MAX_REPAIR_ATTEMPTS = 2


class Orchestrator:
    def __init__(self, router):
        self.router = router

        self.planner = Planner(
            router.get_provider("planner")
        )

        self.builder = Builder(
            router.get_provider("builder")
        )

        self.critic = Critic(
            router.get_provider("critic")
        )

        self.repair = Repair(
            router.get_provider("repair")
        )

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

        while True:
            print("\n--- CRITIC REVIEW ---")

            if agent_calls >= MAX_AGENT_CALLS:
                print("Maximum agent calls reached.")
                return

            critique = self.critic.review(
                task,
                plan,
                result["files"]
            )

            agent_calls += 1

            if not critique:
                print("Critic failed.")
                return

            print("Approved:", critique["approved"])

            if critique["issues"]:
                print("Issues:")

                for issue in critique["issues"]:
                    print("-", issue)

            if critique["approved"]:
                break

            if repair_attempts >= MAX_REPAIR_ATTEMPTS:
                print("\nMaximum repair attempts reached.")
                print("FORGE stopped.")
                return

            if agent_calls >= MAX_AGENT_CALLS:
                print("\nMaximum agent calls reached.")
                print("FORGE stopped.")
                return

            print("\n--- REPAIRING CRITIC ISSUES ---")

            repaired = self.repair.repair(
                task,
                result["files"],
                critic_feedback=critique,
                test_result=None
            )

            agent_calls += 1
            repair_attempts += 1

            if not repaired:
                print("Repair failed.")
                return

            result = repaired

            print(
                f"Repair attempt: "
                f"{repair_attempts}/{MAX_REPAIR_ATTEMPTS}"
            )

        project_dir = Path("generated_project")

        write_files(
            result["files"],
            project_dir
        )

        while True:
            print("\n--- TESTING ---")

            test_result = run_tests(
                project_dir,
                plan["tests"]
            )

            if test_result["success"]:
                print("\nFORGE SUCCESS")
                print("The generated project passed its tests.")
                return

            print("\nTEST FAILED")

            for test in test_result["tests"]:
                if not test["success"]:
                    print("Expected:", test["expected_output"])
                    print("Got:", test["output"])
                    print("Error:", test["error"])

            if repair_attempts >= MAX_REPAIR_ATTEMPTS:
                print("\nMaximum repair attempts reached.")
                print("FORGE stopped.")
                return

            if agent_calls >= MAX_AGENT_CALLS:
                print("\nMaximum agent calls reached.")
                print("FORGE stopped.")
                return

            print("\n--- REPAIRING TEST FAILURE ---")

            repaired = self.repair.repair(
                task,
                result["files"],
                critic_feedback=None,
                test_result=test_result
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