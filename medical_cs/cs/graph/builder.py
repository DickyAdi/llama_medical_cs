from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode

from .node import summarize_conversation, assistant, tools_route, State
from context.app_context import app_context

def graph_builder() -> StateGraph:
    """
    Build and returns a langgraph state machine for the chatbot.
    
    This includes assistant response logic, flow, and in-memory checkpointing.
    
    Returns:
        StateGraph: A langgraph state graph.
    """
    builder = StateGraph(State)
    memory = MemorySaver()
    
    builder.add_node('assistant', lambda state: assistant(state, app_context.llm_with_tools, app_context.vector_stores))
    builder.add_node('tools', ToolNode(app_context.tools))
    builder.add_node('summarize_conv', lambda state: summarize_conversation(state, app_context.llm_with_tools))
    
    builder.add_edge(START, 'assistant')
    builder.add_conditional_edges('assistant', tools_route)
    builder.add_edge('tools', 'assistant')
    builder.add_edge('summarize_conv', END)
    
    state_graph = builder.compile(checkpointer=memory)
    return state_graph

def destroy_graph(state_graph):
    """
    Delete langgraph state graph.
    
    Args:
        state_graph (StateGraph): A state graph which want to be deleted
    """
    if state_graph:
        del state_graph