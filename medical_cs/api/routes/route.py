from langchain_core.messages import HumanMessage

from cs.graph.builder import graph_builder, destroy_graph
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

class chat_request(BaseModel):
    """
    Pydantic chat_request model for validating message given to the chatbot
    
    Attributes:
        message (str) : User input message.
    """
    message: str


state_graph = graph_builder()
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
        response = state_graph.invoke({'messages' : messages}, config)
        return {'response' : response['messages'][-1].content}
    except Exception as e:
        return HTTPException(status_code=500, detail=(str(e)))