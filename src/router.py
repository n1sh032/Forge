class Router:
    def __init__(self, providers):
        self.providers = providers

    def get_provider(self, agent):
        if agent == "planner":
            return self.providers["planner"]

        if agent == "builder":
            return self.providers["builder"]

        if agent == "critic":
            return self.providers["critic"]

        if agent == "repair":
            return self.providers["repair"]

        raise ValueError(f"Unknown agent: {agent}")

    def select_provider(self, agent, task):
        if agent == "planner":
            return self.providers["planner"]

        if agent == "critic":
            return self.providers["critic"]

        if agent == "builder":
            return self.providers["builder"]

        if agent == "repair":
            return self.providers["repair"]

        raise ValueError(f"Unknown agent: {agent}")