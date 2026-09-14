from pathlib import Path

from src.agents.planner import Planner
from src.agents.builder import Builder
from src.agents.critic import Critic
from src.agents.repair import Repair
from src.tools.file_writer import write_files
from src.tools.test_runner import run_tests


MAX_AGENT_CALLS = 10
MAX_REPAIR_ATTEMPTS = 2


class Orchestrator:
    def __init__(self, router):
        self.router = router

    def run(self, task):
        agent_calls = 0
        repair_attempts = 0

        print("\n--- PLANNING ---")

        if agent_calls >= MAX_AGENT_CALLS:
            print("Maximum agent calls reached.")
            return

        planner_provider = self.router.select_provider(
            "planner",
            task
        )

        print(
            "Planner model:",
            planner_provider.model
        )

        planner = Planner(planner_provider)

        plan = planner.make_plan(task)
        agent_calls += 1

        if not plan:
            print("Planning failed.")
            return

        print("\n--- BUILDING ---")

        if agent_calls >= MAX_AGENT_CALLS:
            print("Maximum agent calls reached.")
            return

        builder_provider = self.router.select_provider(
            "builder",
            task
        )

        print(
            "Builder model:",
            builder_provider.model
        )

        builder = Builder(builder_provider)

        result = builder.build(task, plan)
        agent_calls += 1

        if not result:
            print("Building failed.")
            return

        while True:
            print("\n--- CRITIC REVIEW ---")

            if agent_calls >= MAX_AGENT_CALLS:
                print("Maximum agent calls reached.")
                return

            critic_provider = self.router.select_provider(
                "critic",
                task
            )

            print(
                "Critic model:",
                critic_provider.model
            )

            critic = Critic(critic_provider)

            critique = critic.review(
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

            repair_provider = self.router.select_provider(
                "repair",
                task
            )

            print(
                "Repair model:",
                repair_provider.model
            )

            repair = Repair(repair_provider)

            repaired = repair.repair(
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

            repair_provider = self.router.select_provider(
                "repair",
                task
            )

            print(
                "Repair model:",
                repair_provider.model
            )

            repair = Repair(repair_provider)

            repaired = repair.repair(
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