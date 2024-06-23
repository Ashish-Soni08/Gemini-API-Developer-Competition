# Nothing About Us without Us (A Scientic Study by Aidana Rakhatbekova)

The purpoee of the Project is to

Gemini-API-Developer-Competition

organized by [DEVPOST](https://googleai.devpost.com/)

**GRANTED ACCESS TO THE GEMINI 1.5 PRO API AND FILE API:** 29.03.2024

## Environment Setup

```bash

# python version -> 3.10.13
python -V 

# create a environment named -> google-ai
python -m venv google-ai

```

```bash

# activate the environment
source google-ai/bin/activate

```

## UNDERSTANDING THE STRUCTURE OF THE THESIS PDF

## TECHNICAL DETAILS ABOUT THE IMPLEMENTATION

**Gemini 1.5 Pro** is a next-generation AI model that delivers a breakthrough in long context understanding. It can process upto **1M token window** across different modalities, enabling richer and more complex interactions. To put things into Prespective, one can use it to:

- extract insights from `30k+ lines of code`
- 1 hour video
- extract information from `11 hours of audio files`
- even from a `document with 700k words`

**Files API** is an easy way for developers to upload files for multimodel use cases. It’s the most stable and least error-prone method of unlocking multimodel support in your applications using Gemini.

Known Limitations:

- Maximum request size: The **Gemini 1.5 Pro API** currently has a maximum request size of 20MB. Use the **File API** for requests larger than 20MB.

## Tech Stack Components

**Data Framework** - *LlamaIndex*  for extended RAG(Retrieval Augmented Generation) functionality
**Frontend Framework** - *Streamlit*  
**LLM(Large Language Model)** - *Gemini 1.5 Pro* language model from Google
**Programming Language** - *Python*  
**Vector Database** - *Qdrant*
