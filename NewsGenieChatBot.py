# ---- NewsGenieChatBot.py ----
# Import necessary libraries
import streamlit as st
import os
import pprint
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

from state_NewsG import SearchState, SearchStateInput, SearchStateOutput
from workflow_NewsG import build_workflow, visualize_workflow


# Get the API keys
OPENAI_API_KEY = "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"#db.secrets.get(name="OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["SERPER_API_KEY"] = "4b23f7490bfed268729f06d5c2158d3845fa1237"



# Main Streamlit Function
def run_streamlit_app():
    """Streamlit UI for AI Powered News Assistant Chatbot."""
    # page config
    st.set_page_config(page_title="AI Powered News Assitant", layout='wide', page_icon="🤖")
    st.markdown(
        """
        <style>
        .stContainer {
            background-color: #000000;
            color: #ffffff;
            position: top;
        }
        .stTitle {
            color: #ffffff;
            font-size: 2rem;
            font-weight: bold;
            position: relative;
        }
        </style>""",
        unsafe_allow_html=True,
    )

    st.title("🌎:blue[**NewsGenie: The AI Bot**]")
    st.write("""👋:green[Welcome to NewsGenie! An AI Chatbot who helps connect you to the fast pacing world.]""")
    st.write(":violet-badge[**_At your service..._**]")

    st.markdown("""
        <style>
        [data-testid="stHeader"] {
            background: #000000;
        }
        </style>""",
        unsafe_allow_html=True) 
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #000000;
        }
        .stTitle {
        color: #ffffff;
        font-size: 2rem;
        font-weight: bold;
        position: fixed;
        }
        </style>""",
        unsafe_allow_html=True,
    )
   
    # Create two columns for layout
    left_col, main_col = st.columns([0.05, 5])
    
    question = ""
    template = ""

    m = st.markdown("""
        <style>
            [data-testid=stSidebar] {
                background-color: rgb(0, 10, 30);
            }
            div[data-baseweb="listbox"] > ul {
                background-color: green;
                border-color: #2d408d;
            }
            div[data-baseweb="select"] > div {
                background-color: #12222f;
                color: #ffffff;
            }
        </style>
        """, unsafe_allow_html=True)
    
    ## Sidebar 
    with st.sidebar:
            news_category = ['Politics','Business & Finance','Technology','Science', 'Health', 'Entertainment', 'Sports', 'Fashion']
            m = st.markdown(
            """
            <style>
            .selectBox > div:first-child {
            background-color: #red;
            font-weight:bold;
            }
            </style>""", unsafe_allow_html=True) 
            m = st.markdown("""
            <style>
                [data-testid="listbox"] > ul {
                    background-color: green;
                    border-color: #2d408d;
                }</style>""", unsafe_allow_html=True)
            
            category = st.selectbox("Choose Category", news_category)
            chat_prompt = f'''
            You are an AI ChatBot intended to help users with daily news updates.
            \nTOPIC: {category} 
            \nUSER MESSAGE: "Get me the news updates on: {category}"
        '''
        
            m = st.markdown("""
                <style>
                div.stButton > button:first-child {
                    background-color: rgb(33, 55, 77);
                    color: white;
                    border-radius:10px 10px 10px 10px;
                }
                </style>""", unsafe_allow_html=True)

            st.header("Find News")
            # Only when a news category is selected
            if category:
                if st.button("Find Headline"):
                    #template = ChatPromptTemplate.from_messages([("human", "Get me the news updates on {category}"), ])
                    template = "Tell me today's headlines in {topic}."
                if st.button("Find Updates"):
                    template = "Tell me today's updates in {topic}."
                prompt_template = PromptTemplate.from_template(template)
                formatted_prompt = prompt_template.format(topic = category)
                question = formatted_prompt#chat_prompt(category = "sports")#get_response_category()
                
            if st.button(":blue-background[Clear Chat]"):
                st.session_state.messages = []
        
    if question:
        build_graph = build_workflow()
        response_state = build_graph.invoke({"query": question})
        view_graph = visualize_workflow()
                        
  
    # # Custom CSS 
    # st.markdown(
    #     '''
    #     <style>
    #     .streamlit-expanderHeader {
    #         background-color: white;
    #         color: black; # Adjust this for expander header color
    #     }
    #     .streamlit-expanderContent {
    #         background-color: green;
    #         color: white; # Expander content color
    #     }
    #     </style>
    #     ''',
    #     unsafe_allow_html=True
    # )

    with main_col:        
        # with st.expander("Show news for {}".format(news_category), expanded=True):
        #     # Add Buttons to upload image
        #     if st.button(":blue[Upload Image]", key="upload_image"):
        #         st.write("Image upload functionality is not implemented yet.")
        #         uploaded_file = st.file_uploader("Upload image file", type=["jpg", "jpeg", "png", "gif", "webp"])
        #         if uploaded_file is not None:
        #             st.write("Success.")
        #             st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
        m = st.markdown(
            """
            <style>
            .stChatInput > div{
            background-color: #122222;
            color: #333333;
            }
            </style>""", unsafe_allow_html=True) 
        
        # Get the user's input
        question = st.chat_input("Start a conversation!")
        if question:
            build_graph = build_workflow()
            response_state = build_graph.invoke({"query": question})
            view_graph = visualize_workflow()

    return


if __name__ == "__main__":
    run_streamlit_app()

