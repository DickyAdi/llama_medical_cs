from langgraph.graph.message import MessagesState
from langgraph.graph import END
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, RemoveMessage
from typing import Optional

from cs.tools import agent
from cs.rag.retriever import retrieve_context

class State(MessagesState):
    """
    A customised MessagesState by extending langgraph MessagesState.
    
    Attributes:
        summary (str): Summary of previous multiturn conversation (Optional)
    """
    summary:Optional[str]

def summarize_conversation(state:State, llm_with_tools):
    """
    Create or extend a summary from a multiturn conversation.
    Summary will be created or extended and the conversation will only be keep from the last 10 newest multiturn conversation.
    
    Args:
        state (State): A state graph State.
        llm_with_tools: Ollama LLM instance.
    
    Returns:
        dict: A dictionary containing the summary and messages of previous 10 multiturn conversation.
    """
    summary = state.get('summary', '')
    if summary:
        summary_message = (
            f"This is summary of the conversation to date: {summary}\n\n"
            "Extend the summary by taking into account the new messages above."
        )
    else:
        summary_message = "Create a summary of the conversation above."
    messages = state['messages'] + [HumanMessage(content=summary_message)]
    response = llm_with_tools.invoke(messages)
    delete_messages = [RemoveMessage(id=m.id) for m in state['messages'][:-10]]
    return {'summary' : response.content, 'messages' : delete_messages}

def assistant(state:State, llm_with_tools, vector_store):
    """
    An assistant node which will be the entry point of the chatbot.
    
    Args:
        state (State): A state graph State.
        llm_with_tools: Ollama LLM instance.
        
    Returns:
        dict: A dictionary containing the response of the chatbot.
    """
    summary = state.get('summary', '')
    rag_context = retrieve_context(state['messages'][-1].content, vector_store)
    system_prompt = """
    You are an intelligent assistant designed to answer queries efficiently. You have access to specific tools, but you should only use them when absolutely necessary.  

    Before calling a tool, evaluate the user's query carefully. If you can provide a complete and accurate response using your own reasoning and knowledge, do so without invoking any tools. If there's an error when calling a tool and its not related to user input, just ignore it without saying the error to the user.

    Your priority is to deliver precise and well-reasoned answers while minimizing unnecessary tool usage.
    
    If you're unsure or the user's question cannot be answered from your own reasoning and knowledge, you may refer to the additional context below.
    
    {context}
    """.format(context=rag_context)
    if summary:
        summary_sentence = f"\nSummary of conversation earlier: {summary}"
        system_prompt += summary_sentence
    sys_message = [SystemMessage(content=system_prompt)]
    return {'messages' : [llm_with_tools.invoke(sys_message + state['messages'])]}

def tools_route(state:State, messages_key:str='messages'):
    """
    Langgraph state machine routes.
    This will route the state of the state machine including controlling how many multiturn conversation needs to be summarized.
    
    Args:
        state (State): A state graph state
        messages_key (str): Name of the messages key in the state. Default is messages.
    
    Returns:
        str: Will return one of below.
        1. `tools` if there's tool_calls attribute in the state.
        2. `summarize_conv` if 10 multiturn conversation is reached.
        3. END if above 2 terms isn't achieved.
    """
    if isinstance(state, list):
        ai_message = state[-1]
    elif isinstance(state, dict) and (messages := state.get(messages_key, [])):
        ai_message = messages[-1]
    elif messages := getattr(state, messages_key, []):
        ai_message = messages[-1]
    else:
        raise ValueError(f'No messages found in input state to tool_edge: {state}')
    if hasattr(ai_message, 'tool_calls') and len(ai_message.tool_calls) > 0:
        return 'tools'
    if len(state.get('messages', [])) > 10:
        return 'summarize_conv'
    return END