from typing import List

from llama_parse import LlamaParse
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.embeddings.gemini import GeminiEmbedding



from backend.constants import (EMBEDDING_MODEL,
                       GEMINIPRO_API_KEY,
                       LLAMAPARSE_API_KEY,
                       QDRANT_API_KEY,
                       QDRANT_CLUSTER)
                       


###### ETL PIPELINE ######

def extract_markdown_from_pdf(api_key: str = LLAMAPARSE_API_KEY, file_path: str = "data/Master_Thesis_Aidana.pdf", result_type: str = "markdown"):
    
    parser = LlamaParse(
        api_key = api_key,
        result_type = result_type # "markdown" and "text" are available
        )  

    documents = parser.load_data(file_path)

    print("Total Number of Documents parsed ->", len(documents))

def transform_markdown_to_nodes(docs: List):

    markdown_parser = MarkdownNodeParser()
    nodes = markdown_parser.get_nodes_from_documents(docs, include_metadata=True, include_prev_next_rel=True)
    print("Total Number of Nodes created ->", len(nodes))

def load_to_qdrant():
    pass