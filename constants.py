from dotenv import dotenv_values

config = dotenv_values(".env")

# API KEYS, URLS, TOKENS, ETC

## LlamaIndex(LlamaParse)
LLAMAPARSE_API_KEY: str = config["LLAMAPARSE_API"]

## Google(Gemini-1.5-pro-latest)
GEMINIPRO_API_KEY: str = config["GEMINIPRO_API"]

## LangChain(Langsmith)
LANGCHAIN_API_KEY: str = config["LANGCHAIN_API"]
LANGCHAIN_URL: str = config["LANGCHAIN_ENDPOINT"]
LANGCHAIN_PROJECT: str = config["LANGCHAIN_PROJECT"]

## Qdrant
QDRANT_API_KEY: str = config["QDRANT_API"]
QDRANT_CLUSTER: str = config["QDRANT_ENDPOINT"]

# MODELS

EMBEDDING_MODEL = "models/embedding-001"

LLM = "models/gemini-1.5-pro-latest"