from dotenv import load_dotenv
from pathlib import Path
import os
from fastapi import FastAPI
from api.routes.route import router

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

app = FastAPI()
app.include_router(router)