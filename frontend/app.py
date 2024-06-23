########## IMPORTS ##########
import os


# Streamlit 
import streamlit as st
import streamlit_antd_components as sac
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_lottie import st_lottie
from streamlit_pdf_viewer import pdf_viewer
import streamlit_shadcn_ui as ui


from backend.constants import (LANGCHAIN_API_KEY,
                       LANGCHAIN_PROJECT,
                       LANGCHAIN_URL)

from backend.utils import load_lottieurl
#############################
 

#################### ENVIRONMENT VARIABLES ####################
# Set environment variables to enable logging and tracing in LangSmith
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY

os.environ["LANGCHAIN_TRACING_V2"] = "true"

os.environ["LANGCHAIN_ENDPOINT"] = LANGCHAIN_URL

os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT
################################################################
  

############# PAGE CONFIGURATION #############
st.set_page_config(page_title="Nothing About US, Without US", page_icon="random", layout="wide", initial_sidebar_state="expanded", 
                   menu_items={"Report a bug": "https://github.com/Ashish-Soni08/Google-AI-Hackathon/issues", 
                               "About": "# Nothing About Us, Without Us" # TODO: Write a good about message
                               }
                    )
###############################################
  
############# SIDE BAR #######################  

lottie_anime = load_lottieurl("https://lottie.host/ad7e1c48-37c4-4286-92eb-8393eb31616a/1g3Sdho3Oz.json")

with st.sidebar:
    st_lottie(lottie_anime, height=230)
    st.markdown("""**:blue[Nothing About US, Without US]**""")
    # sac.menu([
    #     sac.MenuItem('About the Author', icon='code-square', children=[
    #         sac.MenuItem('Github', icon='github', href='https://github.com/Ashish-Soni08'),
    #         sac.MenuItem('Twitter', icon='twitter', href='https://twitter.com/Ashish_Soni08'),
    #         sac.MenuItem('Linkedin', icon='linkedin', href='https://www.linkedin.com/in/soni-ashish-2091/'),
    #         sac.MenuItem('Hugging Face', icon='hypnotize', href='https://huggingface.co/Ashish08')]),
    #         sac.MenuItem(type='divider'),
    #         sac.MenuItem('Built using', icon='wrench-adjustable-circle-fill', children=[
    #             sac.MenuItem('Google AI', icon='c-circle-fill', href='https://ai.google.dev/'),
    #             sac.MenuItem('LlamaIndex', icon='tools', href='https://www.llamaindex.ai/'),
    #             sac.MenuItem('Streamlit', icon='magic', href='https://streamlit.io/')]),
    #         ], 
    # size='lg', variant='filled', open_all=False)

###############################################

  

############# APP TITLE  #############

# Add CSS styling to center the title
st.markdown("""<style>.title {text-align: center; /* Center title text */}</style>""", unsafe_allow_html=True) 
# Display the title in the middle of the page
st.markdown("<h1 class='title' style='color: purple;'><em>Nothing About Us: Without Us</em> <br> <em>  </em></h1>", unsafe_allow_html=True)

# display_image, begin_chat = st.columns([0.7, 0.3], gap = 'medium')
# with display_image:
#     with st.container(height = 600, border = True):
#         st.image('images/Indigenous_People_Sakha_Buryatia.jpg', use_column_width = 'auto', clamp = True, caption = 'Sunrise by the mountains')

# with begin_chat:
#     st.page_link("pages/chatbot.py", label="Let's Learn", icon="🚀", help="Learn about the topic", use_container_width=True)


###############################################
pdf_widget, chatbot_widget = st.columns(2, gap = 'medium')
with pdf_widget:
    with st.container(height = 800, border = True):
        pdf_viewer(input="data/Master_Thesis_Aidana_Rakhatbekova.pdf", width=700)

    
with chatbot_widget:
    with st.container(height = 800, border = True):

        st.session_state.messages = []
        # Initialize chat history
        if "messages" not in st.session_state:
            pass
    
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
        if prompt := st.chat_input("What's up?"):
        # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
        
        # Simulate stream of response with milliseconds delay
        # streaming_response = query_engine.query(prompt)
        
        # for chunk in streaming_response.response_gen:
        #     full_response += chunk
        #     message_placeholder.markdown(full_response + "▌")

        # full_response = query_engine.query(prompt)

        message_placeholder.markdown(full_response)
        # st.session_state.context = ctx

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})