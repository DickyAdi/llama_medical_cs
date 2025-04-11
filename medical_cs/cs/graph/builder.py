from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode

from .node import summarize_conversation, assistant, tools_route, State, tools

def graph_builder():
    builder = StateGraph(State)
    memory = MemorySaver()
    
    builder.add_node('assistant', assistant)
    builder.add_node('tools', ToolNode(tools))
    builder.add_node('summarize_conv', summarize_conversation)
    
    builder.add_edge(START, 'assistant')
    builder.add_conditional_edges('assistant', tools_route)
    builder.add_edge('tools', 'assistant')
    builder.add_edge('summarize_conv', END)
    
    state_graph = builder.compile(checkpointer=memory)
    return state_graph

def destroy_graph(state_graph):
    if state_graph:
        del state_graph