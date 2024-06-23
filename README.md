# Gemini-API-Developer-Competition

organized by [Google](https://ai.google.dev/competition)

**Gemini 1.5 Pro** is a next-generation AI model that delivers a breakthrough in long context understanding. It can process upto **1M tokens** across different modalities, enabling richer and more complex interactions.

**Files API** is an easy way for developers to upload files for multimodel use cases. It’s the most stable and least error-prone method of unlocking multimodel support in your applications using Gemini.

Known Limitations:

- Maximum request size: The **Gemini 1.5 Pro API** currently has a maximum request size of 20MB. Use the **File API** for requests larger than 20MB.

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

```python

# List models to see the available Gemini models
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

# Output
# models/gemini-1.0-pro
# models/gemini-1.0-pro-001
# models/gemini-1.0-pro-latest
# models/gemini-1.0-pro-vision-latest
# models/gemini-1.0-ultra-latest
# models/gemini-1.5-pro-latest
# models/gemini-pro
# models/gemini-pro-vision
# models/gemini-ultra

```

## Tech Stack

**Data Framework** - **LllamaIndex**  
**Google Generative AI Model** - **Gemini 1.5 Pro**  
**Frontend** - **Streamlit**  
**Programming Language** - **Python**
