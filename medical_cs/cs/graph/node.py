from langgraph.graph.message import MessagesState
from langgraph.graph import END
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, RemoveMessage
from typing import Optional

from cs.tools import agent

tools = [agent.check_schedule, agent.check_specialist_schedule, agent.validate_booking]

llm = ChatOllama(
    model="llama3.2:3b-tool",
    temperature=0
)
llm_with_tools = llm.bind_tools(tools)

class State(MessagesState):
    summary:Optional[str]

def summarize_conversation(state:State):
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

def assistant(state:State):
    summary = state.get('summary', '')
    system_prompt = """
    You are an intelligent assistant designed to answer queries efficiently. You have access to specific tools, but you should only use them when absolutely necessary.  

    Before calling a tool, evaluate the user's query carefully. If you can provide a complete and accurate response using your own reasoning and knowledge, do so without invoking any tools. If there's an error when calling a tool and its not related to user input, just ignore it without saying the error to the user.

    Your priority is to deliver precise and well-reasoned answers while minimizing unnecessary tool usage.  
    """
    if summary:
        summary_sentence = f"\nSummary of conversation earlier: {summary}"
        system_prompt += summary_sentence
    sys_message = [SystemMessage(content=system_prompt)]
    return {'messages' : [llm_with_tools.invoke(sys_message + state['messages'])]}

def tools_route(state:State, messages_key:str='messages'):
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