#################################################################################
# Built-In modules
import os

# Community modules
# from langchain.chains import LLMChain
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
import google.generativeai as genai



# from openai import OpenAI
# import requests

# User-Defined modules
from constants import (LLAMAPARSE_API_KEY,
                       GEMINIPRO_API_KEY)


# from models import (gpt35_turbo_llm,
#                     gpt4_llm,
#                     gpt4_turbo_llm,
#                     gpt4_vision_llm
#                     )

# # Set environment variables to enable logging and tracing in LangSmith 
# os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_ENDPOINT"] = LANGCHAIN_URL
# os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT

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

# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")

print(response.text)