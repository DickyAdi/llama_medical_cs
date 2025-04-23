from dotenv import load_dotenv
from pathlib import Path
import os
from fastapi import FastAPI
from api.routes.route import router
from context.app_context import app_context
from contextlib import asynccontextmanager

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app_context.load_resources()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)