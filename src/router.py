class Router:
    def __init__(self, providers):
        self.providers = providers

        self.provider_profiles = {
            "openai": {
                "reasoning": 10,
                "coding": 9,
                "speed": 7,
                "simple": 7
            },
            "gemini": {
                "reasoning": 8,
                "coding": 10,
                "speed": 9,
                "simple": 9
            }
        }

    def classify_task(self, task):
        task = task.lower()

        complex_words = [
            "authentication",
            "database",
            "api",
            "machine learning",
            "neural network",
            "multi-agent",
            "distributed",
            "concurrent",
            "deployment"
        ]

        medium_words = [
            "file",
            "csv",
            "json",
            "web scraper",
            "calculator",
            "cli",
            "automation"
        ]

        for word in complex_words:
            if word in task:
                return "complex"

        for word in medium_words:
            if word in task:
                return "medium"

        return "simple"

    def score_provider(self, provider_name, agent, task):
        profile = self.provider_profiles[provider_name]

        complexity = self.classify_task(task)

        score = 0

        if agent == "planner":
            score += profile["reasoning"] * 2

        elif agent == "builder":
            score += profile["coding"] * 2

        elif agent == "critic":
            score += profile["reasoning"] * 2

        elif agent == "repair":
            score += profile["coding"] * 2

        if complexity == "simple":
            score += profile["simple"]

        elif complexity == "medium":
            score += profile["coding"]

        elif complexity == "complex":
            score += profile["reasoning"]

        return score

    def select_provider(self, agent, task):
        best_provider = None
        best_score = -1

        for provider_name, provider in self.providers.items():
            score = self.score_provider(
                provider_name,
                agent,
                task
            )

            if score > best_score:
                best_score = score
                best_provider = provider

        return best_provider