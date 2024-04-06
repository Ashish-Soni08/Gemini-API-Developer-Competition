#################################################################################
# Built-In modules
import os

# Community modules
from langchain_google_genai import GoogleGenerativeAI
# from langchain.chains import LLMChain
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
import google.generativeai as genai

# User-Defined modules
from constants import (LLAMAPARSE_API_KEY,
                       LANGCHAIN_API_KEY,
                       LANGCHAIN_PROJECT,
                       LANGCHAIN_URL,
                       GEMINIPRO_API_KEY,
                       QDRANT_API_KEY,
                       QDRANT_CLUSTER)


genai.configure(api_key=GEMINIPRO_API_KEY)

#################################################################################

# template = """
# You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.
# Query: {question}
#  """

# prompt = PromptTemplate(template=template, input_variables=["question"])

# # Create LLM chain
# llm_chain = LLMChain(prompt=prompt, llm=gpt35_turbo_llm)

# question = "Compose a poem that explains the concept of recursion in programming"

# print(llm_chain.invoke(question))



# model = genai.GenerativeModel('gemini-1.5-pro-latest')

# response = model.generate_content("What is the meaning of life?")

# print(response.text)

# Set environment variables to enable logging and tracing in LangSmith 
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = LANGCHAIN_URL
os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT

#### USING LANGCHAIN

llm = GoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=GEMINIPRO_API_KEY)

print(llm.invoke("List 5 reasons to sleep on time everyday. Short and Crisp."))

from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    url=QDRANT_CLUSTER, 
    api_key=QDRANT_API_KEY
)