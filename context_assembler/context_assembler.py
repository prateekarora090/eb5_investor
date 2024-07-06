import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer, util

class ContextAssembler:
    def __init__(self, preprocessed_data_dir):
        self.preprocessed_data_dir = preprocessed_data_dir
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def assemble_context(self, investment_id):
        investment_dir = os.path.join(self.preprocessed_data_dir, investment_id)
        
        # Load metadata
        with open(os.path.join(investment_dir, 'metadata.json'), 'r') as f:
            metadata = json.load(f)
        
        context = {
            'metadata': metadata,
            'documents': [],
            'websites': []
        }

        # Load document chunks
        for file_name in metadata['folder_files']:
            chunks_file = os.path.join(investment_dir, f"{os.path.splitext(file_name)[0]}_chunks.json")
            if os.path.exists(chunks_file):
                with open(chunks_file, 'r') as f:
                    doc_chunks = json.load(f)
                context['documents'].append(doc_chunks)

        # Load website chunks
        for website in metadata['websites']:
            website_file = website.replace('https://', '').replace('http://', '').replace('/', '_')
            chunks_file = os.path.join(investment_dir, f"{website_file}_chunks.json")
            if os.path.exists(chunks_file):
                with open(chunks_file, 'r') as f:
                    website_chunks = json.load(f)
                context['websites'].append(website_chunks)

        return context

    def semantic_search(self, context, query, top_k=5):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        
        results = []
        for doc in context['documents']:
            for chunk in doc['text_chunks']:
                chunk_embedding = self.model.encode(chunk, convert_to_tensor=True)
                similarity = util.pytorch_cos_sim(query_embedding, chunk_embedding)
                results.append((similarity.item(), chunk, doc['name']))
        
        for website in context['websites']:
            for chunk in website['chunks']:
                chunk_embedding = self.model.encode(chunk, convert_to_tensor=True)
                similarity = util.pytorch_cos_sim(query_embedding, chunk_embedding)
                results.append((similarity.item(), chunk, website['url']))
        
        results.sort(reverse=True, key=lambda x: x[0])
        return results[:top_k]

# Usage example
if __name__ == "__main__":
    assembler = ContextAssembler('preprocessing/outputs/preprocessed_data')
    context = assembler.assemble_context('investment_1')
    print(f"Assembled context for investment_1:")
    print(f"Metadata: {context['metadata']}")
    print(f"Number of documents: {len(context['documents'])}")
    print(f"Number of websites: {len(context['websites'])}")
    
    # Example semantic search
    query = "EB-5 visa requirements"
    search_results = assembler.semantic_search(context, query)
    print(f"\nTop 5 results for query '{query}':")
    for similarity, chunk, source in search_results:
        print(f"Similarity: {similarity:.4f}")
        print(f"Source: {source}")
        print(f"Chunk: {chunk[:100]}...")  # Print first 100 characters of the chunk
        print()