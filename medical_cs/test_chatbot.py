from langchain_core.messages import HumanMessage
from context.app_context import app_context
from cs.graph.builder import graph_builder
from dotenv import load_dotenv
from pathlib import Path
import os
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


# Load resources (simulating what FastAPI lifespan does)
app_context.load_resources()

# Build the state graph with the loaded context
state_graph = graph_builder()

# Create a message to test
messages = [HumanMessage(content="What is oncologist specialist schedule?")]

# Invoke the graph
config = {"configurable": {"thread_id": "1"}}
response = state_graph.invoke({"messages": messages}, config)

# Print the chatbot response
# print("Response:", response["messages"])
for m in response['messages']:
    m.pretty_print()