from crewai import Agent

class BaseAgent(Agent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = None

    def set_context(self, context):
        self.context = context

    def semantic_search(self, query, top_k=5):
        if not self.context:
            raise ValueError("Context not set. Call set_context() first.")
        return self.context.semantic_search(query, top_k)

    def deep_dive(self, topic):
        results = self.semantic_search(topic, top_k=10)
        return "\n\n".join([chunk for _, chunk, _ in results])