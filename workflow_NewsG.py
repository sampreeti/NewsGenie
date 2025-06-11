# ---- workflow_NewsG.py ----

## IMPORTS
import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
from langgraph.graph import StateGraph, START, END

from agentNodes import user_request, process_messages, get_response
from state_NewsG import SearchState, SearchStateInput, SearchStateOutput

from dotenv import load_dotenv

load_dotenv()


# Function to build the workflow (Separate from Streamlit logic)
def build_workflow():
    """Build and compile the workflow steps using LangGraph."""
    # Build the workflow for generating responses
    workflow = StateGraph(
        SearchState,
        input=SearchStateInput,
        output=SearchStateOutput) 
    
    # ✅ Add nodes to the workflow
    workflow.add_node("user_request", user_request)
    workflow.add_node("process_messages", process_messages)
    workflow.add_node("get_response", get_response)
       
    # ✅  Add edges to connect the nodes 
    workflow.add_edge(START, "user_request")
    workflow.add_edge("user_request", "process_messages")
    workflow.add_edge("process_messages", "get_response")
    workflow.add_edge("get_response", END)
    
    # Compile the workflow into a chain of actions
    graph = workflow.compile()
    return graph



# Function to visualize the workflow 
def visualize_workflow():
    """Generates a visualization of the workflow graph."""
    graph = nx.DiGraph()
    edges = [
        ("START", "user_request"),
        ("user_request", "process_messages"),
        ("process_messages", "get_response"),
        ("get_response", "END")  # ✅ Last node (no outgoing edges)
    ]
    graph.add_edges_from(edges)
    
    plt.figure(figsize=(8, 5))
    nx.draw(graph, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=2000, font_size=10, font_weight='bold')
    plt.savefig("NewsGenie_Workflow.png")
    
    return "NewsGenie_Workflow.png"