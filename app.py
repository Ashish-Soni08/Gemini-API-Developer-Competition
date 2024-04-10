import os

import streamlit as st

import streamlit_shadcn_ui as ui
import streamlit_antd_components as sac
from streamlit_lottie import st_lottie
from streamlit_extras.add_vertical_space import add_vertical_space

from constants import (LANGCHAIN_API_KEY,
                       LANGCHAIN_PROJECT,
                       LANGCHAIN_URL)

from utils import load_lottieurl

# Set environment variables to enable logging and tracing in LangSmith 
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = LANGCHAIN_URL
os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT

# Page Configuration
st.set_page_config(
    page_title=" - ",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Report a bug': "https://github.com/Ashish-Soni08/Google-AI-Hackathon/issues",
        'About': "# This is a header. This is an *extremely* cool app!" # TODO: Write a good about message 
    }
)

############# SIDE BAR #############
lottie_anime = load_lottieurl("https://lottie.host/ad7e1c48-37c4-4286-92eb-8393eb31616a/1g3Sdho3Oz.json")

with st.sidebar:
    st_lottie(lottie_anime, height=230)
    st.markdown(
        """
    ## 
    **:blue[Sophia]** **Agile AI, Harmonizing Work and Personal Growth**
    """
    )
    
    sac.menu([
    sac.MenuItem('About the Author', icon='code-square', children=[
        sac.MenuItem('Github', icon='github', href="https://github.com/Ashish-Soni08"),
        sac.MenuItem('Twitter', icon='twitter', href="https://twitter.com/Ashish_Soni08"),
        sac.MenuItem('Linkedin', icon='linkedin', href="https://www.linkedin.com/in/soni-ashish-2091/"),
        sac.MenuItem('Hugging Face', icon='hypnotize', href="https://huggingface.co/Ashish08")
        ]),
    
        sac.MenuItem(type='divider'),
        
    sac.MenuItem('Built using', icon='wrench-adjustable-circle-fill', children=[
        sac.MenuItem('Google AI', icon='c-circle-fill', href="https://ai.google.dev/"),
        sac.MenuItem('LlamaIndex', icon='tools', href="https://www.llamaindex.ai/"),
        sac.MenuItem('Streamlit', icon='magic', href="https://streamlit.io/")
        ]),
    ], 
        size='lg', variant='filled', open_all=False) 
###################################

############# APP TITLE  #############
# Add CSS styling to center the title
st.markdown(
    """
    <style>
        .title {
            text-align: center; /* Center title text */
        }
    </style>
    """,
    unsafe_allow_html=True)

# Display the title in the middle of the page
st.markdown("<h1 class='title' style='color: purple;'><em>: </em> <br> <em>  </em></h1>", unsafe_allow_html=True)
