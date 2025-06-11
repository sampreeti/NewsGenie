# ---- agentNodes.py ----
import time
import os
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool  
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

from state_NewsG import SearchState, SearchStateInput, SearchStateOutput

from dotenv import load_dotenv


# Load environment variables
load_dotenv()

openai_api_key = "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"
os.environ['OPENAI_API_KEY'] = openai_api_key
os.environ["SERPER_API_KEY"] = "4b23f7490bfed268729f06d5c2158d3845fa1237"


def user_request(state: SearchState):

    # Initialize chat history via st.session_state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    # Add the user's query to the chat history
    st.session_state.messages.append({"role": "Human", "content": state["query"]})
    # Display the user's query in the chat message
    with st.chat_message("Human"):
        message = st.session_state.messages[-1]
        st.markdown(message["content"])
    
    return 


def process_messages(state: SearchState):
    
    # Initializing Memory via st.session_state
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory(memory_key="chat_history")
    # Initialize chat history via st.session_state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Style the chat message container to display the query and response
    st.markdown(
            """
            <style>
            .stChatMessage {
                background-color: #111322;
                length: 100%;
                width: 100%;
            }
             .stChatMessage > div:nth-child(1) {
                background-color: #12222f;
            }
            .stMarkdown > div:nth-child(1) {
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    
    return

    
def get_response(state: SearchState):
    # Initialize the OpenAI language model and search tool
    # Define Language Model
    llm = ChatOpenAI(model_name='gpt-4o-mini', temperature=0, max_tokens=256)
    search =  GoogleSerperAPIWrapper()
    
    # Initialize tools
    tools = []
    # Set up the tool for performing web searches in real-time
    search_tool = Tool(
        name="Google Search",
        func=search.run,
        description="Useful for when you need to do a search on the internet to find information that another tool can't find. Be specific with your input or ask about something that is new and latest.",
    )
    tools.append(search_tool)

    # Initialize the conversational agent with the tools and language model
    conversational_agent = initialize_agent(
        agent="conversational-react-description",
        tools=tools,
        llm=llm,
        max_iterations=10,
        memory = st.session_state.memory
    )

    # Generate the AI's response
    with st.chat_message("AI"):
        # Set up the Streamlit callback handler
        st_callback = StreamlitCallbackHandler(st.container())
        message_placeholder = st.empty()
        full_response = ""
        ai_response = conversational_agent.run(state["query"], callbacks=[st_callback])

        # Simulate a streaming response with a slight delay
        for chunk in ai_response.split():
            full_response += chunk + " "
            time.sleep(.03)

            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
     
        # Display the full response
        message_placeholder.info(full_response)

    # Add the AI's response to the chat history
    st.session_state.messages.append({"role": "AI", "content": full_response})

    # Display the Human's query and the AI's response in the chat message history 
    for i in range(len(st.session_state.messages)-3, -1,-2):
        message_Human = st.session_state.messages[i-1]
        message_AI = st.session_state.messages[i]
        with st.chat_message(message_Human["role"]):
                st.markdown(message_Human["content"])
        with st.chat_message(message_AI["role"]):
                st.markdown(message_AI["content"])

    
    return
