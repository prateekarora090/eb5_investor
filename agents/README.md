# Agents Directory

This directory contains the specialized agents used in the EB-5 Investment Analysis system.

## BaseAgent

The `BaseAgent` class (`base_agent.py`) serves as the foundation for all specialized agents. It provides common functionality such as:

- Setting and accessing the investment context
- Performing semantic searches within the context
- Conducting deep dives into specific topics

### Key Methods

- `set_context(context)`: Sets the investment context for the agent.
- `semantic_search(query, top_k=5)`: Performs a semantic search on the context, returning the top_k most relevant results.
- `deep_dive(topic)`: Conducts a more comprehensive search on a specific topic, returning concatenated relevant information.

## Specialized Agents

1. **Financial Analyst** (`financial_analyst.py`): Analyzes financial aspects of EB-5 investments.
2. **Immigration Law Expert** (`immigration_law_expert.py`): Evaluates immigration law compliance for investments.
3. **Risk Assessor** (`risk_assessor.py`): Assesses various risks associated with EB-5 investments.
4. **EB-5 Program Specialist** (`eb5_program_specialist.py`): Evaluates compliance with EB-5 program requirements.

Each specialized agent inherits from `BaseAgent` and implements specific analysis methods relevant to their expertise.

## Usage

Agents are initialized in the main analysis pipeline and are provided with the investment context. They use their specialized knowledge, the provided context, and common tools (semantic search, deep dive) to perform their analyses.

Example usage in the main pipeline:

```python
financial_analyst = FinancialAnalyst(llm=llm)
financial_analyst.set_context(investment_context)
financial_analysis = financial_analyst.analyze()
```

## Extending the System

To add new specialized agents:

1. Create a new Python file for the agent (e.g., `new_specialist.py`).
2. Define a class that inherits from `BaseAgent`.
3. Implement the specialized analysis methods.
4. Update the main analysis pipeline to include the new agent.