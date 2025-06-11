🗞️ NewsGenie: AI-Powered Real-Time News Assistant
	NewsGenie is a stateful, LLM-powered, multimodal news assistant designed to deliver real-time, topic-specific news 	insights by orchestrating an intelligent search-to-summarize pipeline using LangGraph + LangChain, integrated with 	OpenAI GPT-4o-mini and live search APIs like Serper.dev.
	Built with a clean, interactive UI via Streamlit, this system transforms your queries into real-time insights 	through a dynamic and inspectable computation graph.

💡 Features
________________________________________
• Web Search Integration: Uses Serper.dev to fetch the latest real-time news data from the web.
• LLM Orchestration: Streamlined reasoning with OpenAI GPT-4o-mini via LangGraph workflows.
• Composable State Graph: Fully modular LangGraph-based graph enables debugging, visualization, and memory support.
• Topic-Driven Prompting: Tailored prompts for diverse categories such as Technology, Health, Politics, etc.
• Streamlit UI: Clean, theme-customized layout for a pleasant chat experience.
• Session Persistence: In-chat prompt templates with state-aware query routing.


🛠️ Tech Stack
________________________________________
Layer	Tech
Frontend		Streamlit
LLM Orchestration	LangGraph, LangChain Core
LLM Model		gpt-4o-mini via OpenAI API
Search API		Serper.dev (Google Search wrapper)
Prompting		PromptTemplate, ChatPromptTemplate

	

📁 Project Structure
________________________________________
📦 NewsGenie/
├── NewsGenieChatBot.py         	# Streamlit front-end and app logic
├── agentNodes.py               	# Core API functionalities to ensure the data flow
├── state_NewsG.py              	# Custom input/output state schemas for LangGraph
├── workflow_NewsG.py           	# Core LangGraph workflow definition
├── README.md                   	# You're here!

