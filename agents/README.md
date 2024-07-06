# Agents Directory

This directory contains the specialized agents used in the EB-5 Investment Analysis system.

## Base Agent

The `BaseAgent` class serves as the foundation for all specialized agents in the EB-5 investment analysis system. It extends the `Agent` class from the CrewAI framework and provides additional functionality for context handling, semantic search, and web search capabilities.

## Key Features

1. **Context Management**: Set and manage the context for the agent's analysis.
2. **Semantic Search**: Perform semantic searches within the set context.
3. **Deep Dive**: Conduct a more comprehensive search on specific topics.
4. **Web Search**: Perform web searches for additional information.
5. **Memory Operations**: Store and retrieve information in short-term and long-term memory.

## Usage

```python
from agents.base_agent import BaseAgent

class SpecializedAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional initialization for specialized agent

    def analyze(self, context):
        self.set_context(context)
        # Implement specialized analysis logic
```

## Methods

- `set_context(context)`: Set the context for the agent's analysis.
- `semantic_search(query, top_k=5)`: Perform a semantic search within the set context.
- `deep_dive(topic)`: Conduct a more comprehensive search on a specific topic.
- `web_search(query)`: Perform a web search for additional information.
- `add_to_short_term_memory(key, value)`: Store information in short-term memory.
- `add_to_long_term_memory(key, value)`: Store information in long-term memory.
- `get_from_short_term_memory(key)`: Retrieve information from short-term memory.
- `get_from_long_term_memory(key)`: Retrieve information from long-term memory.
- `get_all_long_term_memory()`: Retrieve all information stored in long-term memory.

## Dependencies

- crewai
- requests

Ensure these dependencies are installed before using the BaseAgent.