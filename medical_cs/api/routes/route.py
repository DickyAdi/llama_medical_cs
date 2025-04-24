from langchain_core.messages import HumanMessage
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from cs.graph.builder import graph_builder, destroy_graph
from context.app_context import app_context

class chat_request(BaseModel):
    """
    Pydantic chat_request model for validating message given to the chatbot
    
    Attributes:
        message (str) : User input message.
    """
    message: str

_state_graph = None #state_graph place holder

def get_state_graph():
    """
    Lazy initialization the state graph.
    
    Returns:
        Object: Langgraph state graph.
    """
    global _state_graph
    if _state_graph is None:
        app_context.load_resources()
        _state_graph = graph_builder()
    return _state_graph

router = APIRouter()

@router.post('/chat')
async def chat(request: chat_request):
    """
    Handle a POST request to initiate a chat to a chatbot.
    
    This endpoint sends user's message to the state_graph chatbot and then returns the response from the chatbot to the user.
    
    Args:
        request (chat_request): The incoming message request from the user's.
    Returns:
        dict: A dictionary that contains chatbot response.
    Raises:
        HTTPException: Returns a 500 code HTTPException with detailed error.
    """
    try:
        config = {'configurable' : {'thread_id' : '1'}}
        messages = [HumanMessage(content=request.message)]
        graph = get_state_graph()
        response = graph.invoke({'messages' : messages}, config)
        return {'response' : response['messages'][-1].content}
    except Exception as e:
        return HTTPException(status_code=500, detail=(str(e)))