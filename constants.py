from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
# print(config)

# API KEYS, URLS, TOKENS, ETC

## Data Providers

# LlamaIndex
LLAMAPARSE_API_KEY: str = config["LLAMAPARSE_API"]

# ## Anyscale Endpoints
# ANYSCALE_API_KEY: str = config["ANYSCALE_API"]

## Model Providers

# Google
GEMINIPRO_API_KEY: str = config["GEMINIPRO_API"]

# # Hugging Face
# HF_API_KEY: str = config["HF_API"] # Read
# HF_TOKEN: str = config["HF_TOKEN"] # Write

# # LangChain(langsmith)
# LANGCHAIN_API_KEY: str = config["LANGCHAIN_API"]
# LANGCHAIN_URL: str = config["LANGCHAIN_ENDPOINT"]
# LANGCHAIN_PROJECT: str = config["LANGCHAIN_PROJECT"]