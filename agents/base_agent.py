from crewai import Agent

class BaseAgent:
    def __init__(self, *args, **kwargs):
        self.agent = Agent(*args, **kwargs)
        self.context = None

    def set_context(self, context):
        """
        Set the context for the agent. This should be called before using
        semantic_search or deep_dive methods.
        :param context: The ContextAssembler object containing the investment context.
        """
        self.context = context

    def semantic_search(self, query, top_k=5):
        """
        Perform a semantic search on the agent's context.
        This method returns a list of the top_k most relevant results for the given query.
        Each result is a tuple containing (similarity_score, content_chunk, source).
        :param query: The search query string.
        :param top_k: The number of top results to return (default is 5).
        :return: List of tuples (similarity_score, content_chunk, source).
        """
        if not self.context:
            raise ValueError("Context not set. Call set_context() first.")
        return self.context.semantic_search(self.context, query, top_k)

    def deep_dive(self, topic):
        """
        Perform a more comprehensive search on a specific topic.
        This method retrieves more results than semantic_search and concatenates
        them into a single string, providing a broader context on the topic.
        :param topic: The topic to deep dive into.
        :return: A string containing concatenated relevant information.
        """
        results = self.semantic_search(topic, top_k=10)
        return "\n\n".join([chunk for _, chunk, _ in results])

    def web_search(self, query):
        pass
        # api_key = os.getenv('SEARCH_API_KEY')
        # url = f"https://api.search.com?q={query}&key={api_key}"
        # response = requests.get(url)
        # if response.status_code == 200:
        #     return response.json()['results']
        # else:
        #     raise Exception(f"Web search failed with status code {response.status_code}")

    # Delegate other methods to self.agent as needed
    def __getattr__(self, name):
        return getattr(self.agent, name)