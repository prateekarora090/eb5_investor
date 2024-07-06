# Context Assembler

The `ContextAssembler` class is responsible for assembling and managing the context for EB-5 investment analysis. It provides functionality to load preprocessed data and perform semantic searches within the assembled context.

## Key Features

1. **Context Assembly**: Loads preprocessed data for a given investment ID, including metadata, document chunks, and website content.

2. **Semantic Search**: Performs semantic searches within the assembled context using sentence embeddings.

## Usage

```python
from context_assembler import ContextAssembler

# Initialize the ContextAssembler
assembler = ContextAssembler('path/to/preprocessed_data')

# Assemble context for a specific investment
context = assembler.assemble_context('investment_id')

# Perform a semantic search within the context
results = assembler.semantic_search(context, "search query", top_k=5)
```

## Methods

- `assemble_context(investment_id)`: Assembles the context for a given investment ID.
- `semantic_search(context, query, top_k=5)`: Performs a semantic search within the given context.

## Dependencies

- sentence_transformers
- numpy

Ensure these dependencies are installed before using the ContextAssembler.