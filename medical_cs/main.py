from dotenv import load_dotenv
from pathlib import Path
import os
from fastapi import FastAPI
from api.routes.route import router

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# state_graph = graph_builder()
# config = {'configurable' : {'thread_id' : '1'}}
# messages = [HumanMessage(content='give me the schedule of doctor andi pratama')]
# response = state_graph.invoke({'messages' : messages}, config)
# print(response['messages'][-1].content)

## debugging purpose only
# for m in response['messages']:
#     m.pretty_print()

### FastAPI code below
app = FastAPI()
app.include_router(router)