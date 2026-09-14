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

        else:
            raise ValueError(f"Unknown agent: {agent}")

        if complexity == "simple":
            score += profile["simple"]

        elif complexity == "medium":
            score += profile["coding"]

        elif complexity == "complex":
            score += profile["reasoning"]

        return score

    def route(self, agent, task):
        complexity = self.classify_task(task)

        best_provider = None
        best_provider_name = None
        best_score = -1

        scores = {}

        for provider_name, provider in self.providers.items():

            if provider_name not in self.provider_profiles:
                continue

            score = self.score_provider(
                provider_name,
                agent,
                task
            )

            scores[provider_name] = score

            if score > best_score:
                best_score = score
                best_provider = provider
                best_provider_name = provider_name

        if best_provider is None:
            raise ValueError("No valid providers available")

        return {
            "provider": best_provider,
            "provider_name": best_provider_name,
            "score": best_score,
            "complexity": complexity,
            "scores": scores
        }

    def select_provider(self, agent, task):
        decision = self.route(agent, task)

        return decision["provider"]