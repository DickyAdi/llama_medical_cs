from langchain_core.messages import HumanMessage

from cs.graph.builder import graph_builder, destroy_graph
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

class chat_request(BaseModel):
    message: str


state_graph = graph_builder()
router = APIRouter()

@router.post('/chat')
async def chat(request: chat_request):
    try:
        config = {'configurable' : {'thread_id' : '1'}}
        messages = [HumanMessage(content=request.message)]
        response = state_graph.invoke({'messages' : messages}, config)
        return {'response' : response['messages'][-1].content}
    except Exception as e:
        return HTTPException(status_code=500, detail=(str(e)))
    
